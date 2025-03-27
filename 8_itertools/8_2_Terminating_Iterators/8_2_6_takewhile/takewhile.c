// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L1442


static PyObject *
takewhile_next(PyObject *op)
{
    takewhileobject *lz = takewhileobject_CAST(op);
    PyObject *item, *good;
    PyObject *it = lz->it;
    long ok;

    if (lz->stop == 1)
        return NULL;

    item = (*Py_TYPE(it)->tp_iternext)(it);
    if (item == NULL)
        return NULL;

    good = PyObject_CallOneArg(lz->func, item);
    if (good == NULL) {
        Py_DECREF(item);
        return NULL;
    }
    ok = PyObject_IsTrue(good);
    Py_DECREF(good);
    if (ok > 0)
        return item;
    Py_DECREF(item);
    if (ok == 0)
        lz->stop = 1;
    return NULL;
}