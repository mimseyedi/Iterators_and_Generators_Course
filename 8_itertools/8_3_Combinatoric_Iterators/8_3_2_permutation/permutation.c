// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L2822


static PyObject *
permutations_next(PyObject *op)
{
    permutationsobject *po = permutationsobject_CAST(op);
    PyObject *elem;
    PyObject *oldelem;
    PyObject *pool = po->pool;
    Py_ssize_t *indices = po->indices;
    Py_ssize_t *cycles = po->cycles;
    PyObject *result = po->result;
    Py_ssize_t n = PyTuple_GET_SIZE(pool);
    Py_ssize_t r = po->r;
    Py_ssize_t i, j, k, index;

    if (po->stopped)
        return NULL;

    if (result == NULL) {
        /* On the first pass, initialize result tuple using the indices */
        result = PyTuple_New(r);
        if (result == NULL)
            goto empty;
        po->result = result;
        for (i=0; i<r ; i++) {
            index = indices[i];
            elem = PyTuple_GET_ITEM(pool, index);
            Py_INCREF(elem);
            PyTuple_SET_ITEM(result, i, elem);
        }
    } else {
        if (n == 0)
            goto empty;

        /* Copy the previous result tuple or re-use it if available */
        if (Py_REFCNT(result) > 1) {
            PyObject *old_result = result;
            result = _PyTuple_FromArray(_PyTuple_ITEMS(old_result), r);
            if (result == NULL)
                goto empty;
            po->result = result;
            Py_DECREF(old_result);
        }
        // bpo-42536: The GC may have untracked this result tuple. Since we're
        // recycling it, make sure it's tracked again:
        else if (!_PyObject_GC_IS_TRACKED(result)) {
            _PyObject_GC_TRACK(result);
        }
        /* Now, we've got the only copy so we can update it in-place */
        assert(r == 0 || Py_REFCNT(result) == 1);

        /* Decrement rightmost cycle, moving leftward upon zero rollover */
        for (i=r-1 ; i>=0 ; i--) {
            cycles[i] -= 1;
            if (cycles[i] == 0) {
                /* rotatation: indices[i:] = indices[i+1:] + indices[i:i+1] */
                index = indices[i];
                for (j=i ; j<n-1 ; j++)
                    indices[j] = indices[j+1];
                indices[n-1] = index;
                cycles[i] = n - i;
            } else {
                j = cycles[i];
                index = indices[i];
                indices[i] = indices[n-j];
                indices[n-j] = index;

                for (k=i; k<r ; k++) {
                    /* start with i, the leftmost element that changed */
                    /* yield tuple(pool[k] for k in indices[:r]) */
                    index = indices[k];
                    elem = PyTuple_GET_ITEM(pool, index);
                    Py_INCREF(elem);
                    oldelem = PyTuple_GET_ITEM(result, k);
                    PyTuple_SET_ITEM(result, k, elem);
                    Py_DECREF(oldelem);
                }
                break;
            }
        }
        /* If i is negative, then the cycles have all
           rolled-over and we're done. */
        if (i < 0)
            goto empty;
    }
    return Py_NewRef(result);

empty:
    po->stopped = 1;
    return NULL;
}