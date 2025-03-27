// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L3630


static PyObject *
repeat_next(PyObject *op)
{
    repeatobject *ro = repeatobject_CAST(op);
    if (ro->cnt == 0)
        return NULL;
    if (ro->cnt > 0)
        ro->cnt--;
    return Py_NewRef(ro->element);
}