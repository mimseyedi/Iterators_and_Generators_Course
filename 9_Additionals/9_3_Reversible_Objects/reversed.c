// https://github.com/python/cpython/blob/main/Objects/enumobject.c#L457

static PyObject *
reversed_next(PyObject *op)
{
    reversedobject *ro = _reversedobject_CAST(op);
    PyObject *item;
    Py_ssize_t index = FT_ATOMIC_LOAD_SSIZE_RELAXED(ro->index);

    if (index >= 0) {
        item = PySequence_GetItem(ro->seq, index);
        if (item != NULL) {
            FT_ATOMIC_STORE_SSIZE_RELAXED(ro->index, index - 1);
            return item;
        }
        if (PyErr_ExceptionMatches(PyExc_IndexError) ||
            PyErr_ExceptionMatches(PyExc_StopIteration))
            PyErr_Clear();
    }
    FT_ATOMIC_STORE_SSIZE_RELAXED(ro->index, -1);
#ifndef Py_GIL_DISABLED
    Py_CLEAR(ro->seq);
#endif
    return NULL;
}