// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L190


static PyObject *
batched_next(PyObject *op)
{
    batchedobject *bo = batchedobject_CAST(op);
    Py_ssize_t i;
    Py_ssize_t n = FT_ATOMIC_LOAD_SSIZE_RELAXED(bo->batch_size);
    PyObject *it = bo->it;
    PyObject *item;
    PyObject *result;

    if (n < 0) {
        return NULL;
    }
    result = PyTuple_New(n);
    if (result == NULL) {
        return NULL;
    }
    iternextfunc iternext = *Py_TYPE(it)->tp_iternext;
    PyObject **items = _PyTuple_ITEMS(result);
    for (i=0 ; i < n ; i++) {
        item = iternext(it);
        if (item == NULL) {
            goto null_item;
        }
        items[i] = item;
    }
    return result;

 null_item:
    if (PyErr_Occurred()) {
        if (!PyErr_ExceptionMatches(PyExc_StopIteration)) {
            /* Input raised an exception other than StopIteration */
            FT_ATOMIC_STORE_SSIZE_RELAXED(bo->batch_size, -1);
#ifndef Py_GIL_DISABLED
            Py_CLEAR(bo->it);
#endif
            Py_DECREF(result);
            return NULL;
        }
        PyErr_Clear();
    }
    if (i == 0) {
        FT_ATOMIC_STORE_SSIZE_RELAXED(bo->batch_size, -1);
#ifndef Py_GIL_DISABLED
        Py_CLEAR(bo->it);
#endif
        Py_DECREF(result);
        return NULL;
    }
    if (bo->strict) {
        FT_ATOMIC_STORE_SSIZE_RELAXED(bo->batch_size, -1);
#ifndef Py_GIL_DISABLED
        Py_CLEAR(bo->it);
#endif
        Py_DECREF(result);
        PyErr_SetString(PyExc_ValueError, "batched(): incomplete batch");
        return NULL;
    }
    _PyTuple_Resize(&result, i);
    return result;
}