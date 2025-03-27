// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L3151


static PyObject *
compress_next(PyObject *op)
{
    compressobject *lz = compressobject_CAST(op);
    PyObject *data = lz->data, *selectors = lz->selectors;
    PyObject *datum, *selector;
    PyObject *(*datanext)(PyObject *) = *Py_TYPE(data)->tp_iternext;
    PyObject *(*selectornext)(PyObject *) = *Py_TYPE(selectors)->tp_iternext;
    int ok;

    while (1) {
        /* Steps:  get datum, get selector, evaluate selector.
           Order is important (to match the pure python version
           in terms of which input gets a chance to raise an
           exception first).
        */

        datum = datanext(data);
        if (datum == NULL)
            return NULL;

        selector = selectornext(selectors);
        if (selector == NULL) {
            Py_DECREF(datum);
            return NULL;
        }

        ok = PyObject_IsTrue(selector);
        Py_DECREF(selector);
        if (ok > 0)
            return datum;
        Py_DECREF(datum);
        if (ok < 0)
            return NULL;
    }
}