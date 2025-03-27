// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L2563


static PyObject *
cwr_next(PyObject *op)
{
    cwrobject *co = cwrobject_CAST(op);
    PyObject *elem;
    PyObject *oldelem;
    PyObject *pool = co->pool;
    Py_ssize_t *indices = co->indices;
    PyObject *result = co->result;
    Py_ssize_t n = PyTuple_GET_SIZE(pool);
    Py_ssize_t r = co->r;
    Py_ssize_t i, index;

    if (co->stopped)
        return NULL;

    if (result == NULL) {
        /* On the first pass, initialize result tuple with pool[0] */
        result = PyTuple_New(r);
        if (result == NULL)
            goto empty;
        co->result = result;
        if (n > 0) {
            elem = PyTuple_GET_ITEM(pool, 0);
            for (i=0; i<r ; i++) {
                assert(indices[i] == 0);
                Py_INCREF(elem);
                PyTuple_SET_ITEM(result, i, elem);
            }
        }
    } else {
        /* Copy the previous result tuple or re-use it if available */
        if (Py_REFCNT(result) > 1) {
            PyObject *old_result = result;
            result = _PyTuple_FromArray(_PyTuple_ITEMS(old_result), r);
            if (result == NULL)
                goto empty;
            co->result = result;
            Py_DECREF(old_result);
        }
        // bpo-42536: The GC may have untracked this result tuple. Since we're
        // recycling it, make sure it's tracked again:
        else if (!_PyObject_GC_IS_TRACKED(result)) {
            _PyObject_GC_TRACK(result);
        }
        /* Now, we've got the only copy so we can update it in-place CPython's
           empty tuple is a singleton and cached in PyTuple's freelist. */
        assert(r == 0 || Py_REFCNT(result) == 1);

       /* Scan indices right-to-left until finding one that is not
        * at its maximum (n-1). */
        for (i=r-1 ; i >= 0 && indices[i] == n-1; i--)
            ;

        /* If i is negative, then the indices are all at
           their maximum value and we're done. */
        if (i < 0)
            goto empty;

        /* Increment the current index which we know is not at its
           maximum.  Then set all to the right to the same value. */
        index = indices[i] + 1;
        assert(index < n);
        elem = PyTuple_GET_ITEM(pool, index);
        for ( ; i<r ; i++) {
            indices[i] = index;
            Py_INCREF(elem);
            oldelem = PyTuple_GET_ITEM(result, i);
            PyTuple_SET_ITEM(result, i, elem);
            Py_DECREF(oldelem);
        }
    }

    return Py_NewRef(result);

empty:
    co->stopped = 1;
    return NULL;
}