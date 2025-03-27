// https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c#L3497


static PyObject *
count_next(PyObject *op)
{
    countobject *lz = countobject_CAST(op);
#ifndef Py_GIL_DISABLED
    if (lz->cnt == PY_SSIZE_T_MAX)
        return count_nextlong(lz);
    return PyLong_FromSsize_t(lz->cnt++);
#else
    // free-threading version
    // fast mode uses compare-exchange loop
    // slow mode uses a critical section
    PyObject *returned;
    Py_ssize_t cnt;

    cnt = _Py_atomic_load_ssize_relaxed(&lz->cnt);
    for (;;) {
        if (cnt == PY_SSIZE_T_MAX) {
            Py_BEGIN_CRITICAL_SECTION(lz);
            returned = count_nextlong(lz);
            Py_END_CRITICAL_SECTION();
            return returned;
        }
        if (_Py_atomic_compare_exchange_ssize(&lz->cnt, &cnt, cnt + 1)) {
            return PyLong_FromSsize_t(cnt);
        }
    }
#endif
}