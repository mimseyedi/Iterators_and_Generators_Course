// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L346


static PyObject *
pairwise_next(PyObject *op)
{
    pairwiseobject *po = pairwiseobject_CAST(op);
    PyObject *it = po->it;
    PyObject *old = po->old;
    PyObject *new, *result;

    if (it == NULL) {
        return NULL;
    }
    if (old == NULL) {
        old = (*Py_TYPE(it)->tp_iternext)(it);
        Py_XSETREF(po->old, old);
        if (old == NULL) {
            Py_CLEAR(po->it);
            return NULL;
        }
        it = po->it;
        if (it == NULL) {
            Py_CLEAR(po->old);
            return NULL;
        }
    }
    Py_INCREF(old);
    new = (*Py_TYPE(it)->tp_iternext)(it);
    if (new == NULL) {
        Py_CLEAR(po->it);
        Py_CLEAR(po->old);
        Py_DECREF(old);
        return NULL;
    }

    result = po->result;
    if (Py_REFCNT(result) == 1) {
        Py_INCREF(result);
        PyObject *last_old = PyTuple_GET_ITEM(result, 0);
        PyObject *last_new = PyTuple_GET_ITEM(result, 1);
        PyTuple_SET_ITEM(result, 0, Py_NewRef(old));
        PyTuple_SET_ITEM(result, 1, Py_NewRef(new));
        Py_DECREF(last_old);
        Py_DECREF(last_new);
        // bpo-42536: The GC may have untracked this result tuple. Since we're
        // recycling it, make sure it's tracked again:
        if (!_PyObject_GC_IS_TRACKED(result)) {
            _PyObject_GC_TRACK(result);
        }
    }
    else {
        result = PyTuple_New(2);
        if (result != NULL) {
            PyTuple_SET_ITEM(result, 0, Py_NewRef(old));
            PyTuple_SET_ITEM(result, 1, Py_NewRef(new));
        }
    }

    Py_XSETREF(po->old, new);
    Py_DECREF(old);
    return result;
}