// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L1199


static PyObject *
cycle_next(PyObject *op)
{
    cycleobject *lz = cycleobject_CAST(op);
    PyObject *item;

    if (lz->it != NULL) {
        item = PyIter_Next(lz->it);
        if (item != NULL) {
            if (lz->firstpass)
                return item;
            if (PyList_Append(lz->saved, item)) {
                Py_DECREF(item);
                return NULL;
            }
            return item;
        }
        /* Note:  StopIteration is already cleared by PyIter_Next() */
        if (PyErr_Occurred())
            return NULL;
        Py_CLEAR(lz->it);
    }
    if (PyList_GET_SIZE(lz->saved) == 0)
        return NULL;
    item = PyList_GET_ITEM(lz->saved, lz->index);
    lz->index++;
    if (lz->index >= PyList_GET_SIZE(lz->saved))
        lz->index = 0;
    return Py_NewRef(item);
}