// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L1881


static PyObject *
chain_next(PyObject *op)
{
    chainobject *lz = chainobject_CAST(op);
    PyObject *item;

    /* lz->source is the iterator of iterables. If it's NULL, we've already
     * consumed them all. lz->active is the current iterator. If it's NULL,
     * we should grab a new one from lz->source. */
    while (lz->source != NULL) {
        if (lz->active == NULL) {
            PyObject *iterable = PyIter_Next(lz->source);
            if (iterable == NULL) {
                Py_CLEAR(lz->source);
                return NULL;            /* no more input sources */
            }
            lz->active = PyObject_GetIter(iterable);
            Py_DECREF(iterable);
            if (lz->active == NULL) {
                Py_CLEAR(lz->source);
                return NULL;            /* input not iterable */
            }
        }
        item = (*Py_TYPE(lz->active)->tp_iternext)(lz->active);
        if (item != NULL)
            return item;
        if (PyErr_Occurred()) {
            if (PyErr_ExceptionMatches(PyExc_StopIteration))
                PyErr_Clear();
            else
                return NULL;            /* input raised an exception */
        }
        /* lz->active is consumed, try with the next iterable. */
        Py_CLEAR(lz->active);
    }
    /* Everything had been consumed already. */
    return NULL;
}