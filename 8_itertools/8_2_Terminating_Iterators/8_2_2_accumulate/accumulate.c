// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L3019


static PyObject *
accumulate_next(PyObject *op)
{
    accumulateobject *lz = accumulateobject_CAST(op);
    PyObject *val, *newtotal;

    if (lz->initial != Py_None) {
        lz->total = lz->initial;
        lz->initial = Py_NewRef(Py_None);
        return Py_NewRef(lz->total);
    }
    val = (*Py_TYPE(lz->it)->tp_iternext)(lz->it);
    if (val == NULL)
        return NULL;

    if (lz->total == NULL) {
        lz->total = Py_NewRef(val);
        return lz->total;
    }

    if (lz->binop == NULL)
        newtotal = PyNumber_Add(lz->total, val);
    else
        newtotal = PyObject_CallFunctionObjArgs(lz->binop, lz->total, val, NULL);
    Py_DECREF(val);
    if (newtotal == NULL)
        return NULL;

    Py_INCREF(newtotal);
    Py_SETREF(lz->total, newtotal);
    return newtotal;
}