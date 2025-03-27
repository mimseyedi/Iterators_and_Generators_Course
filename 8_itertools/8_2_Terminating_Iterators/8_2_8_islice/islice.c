// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L1613


static PyObject *
islice_next(PyObject *op)
{
    isliceobject *lz = isliceobject_CAST(op);
    PyObject *item;
    PyObject *it = lz->it;
    Py_ssize_t stop = lz->stop;
    Py_ssize_t oldnext;
    PyObject *(*iternext)(PyObject *);

    if (it == NULL)
        return NULL;

    iternext = *Py_TYPE(it)->tp_iternext;
    while (lz->cnt < lz->next) {
        item = iternext(it);
        if (item == NULL)
            goto empty;
        Py_DECREF(item);
        lz->cnt++;
    }
    if (stop != -1 && lz->cnt >= stop)
        goto empty;
    item = iternext(it);
    if (item == NULL)
        goto empty;
    lz->cnt++;
    oldnext = lz->next;
    /* The (size_t) cast below avoids the danger of undefined
       behaviour from signed integer overflow. */
    lz->next += (size_t)lz->step;
    if (lz->next < oldnext || (stop != -1 && lz->next > stop))
        lz->next = stop;
    return item;

empty:
    Py_CLEAR(lz->it);
    return NULL;
}