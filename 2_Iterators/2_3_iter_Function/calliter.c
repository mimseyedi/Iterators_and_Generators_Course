// https://github.com/python/cpython/blob/main/Objects/iterobject.c#L215


static PyObject *
calliter_iternext(calliterobject *it)
{
    PyObject *result;

    if (it->it_callable == NULL) {
        return NULL;
    }

    result = _PyObject_CallNoArgs(it->it_callable);
    if (result != NULL && it->it_sentinel != NULL){
        int ok;

        ok = PyObject_RichCompareBool(it->it_sentinel, result, Py_EQ);
        if (ok == 0) {
            return result; /* Common case, fast path */
        }

        if (ok > 0) {
            Py_CLEAR(it->it_callable);
            Py_CLEAR(it->it_sentinel);
        }
    }
    else if (PyErr_ExceptionMatches(PyExc_StopIteration)) {
        PyErr_Clear();
        Py_CLEAR(it->it_callable);
        Py_CLEAR(it->it_sentinel);
    }
    Py_XDECREF(result);
    return NULL;
}