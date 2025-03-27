// https://github.com/python/cpython/blob/main/Objects/genobject.c#L595


static PyObject *
_gen_throw(PyGenObject *gen, int close_on_genexit,
           PyObject *typ, PyObject *val, PyObject *tb)
{
    PyObject *yf = _PyGen_yf(gen);

    if (yf) {
        _PyInterpreterFrame *frame = &gen->gi_iframe;
        PyObject *ret;
        int err;
        if (PyErr_GivenExceptionMatches(typ, PyExc_GeneratorExit) &&
            close_on_genexit
        ) {
            /* Asynchronous generators *should not* be closed right away.
               We have to allow some awaits to work it through, hence the
               `close_on_genexit` parameter here.
            */
            PyFrameState state = gen->gi_frame_state;
            gen->gi_frame_state = FRAME_EXECUTING;
            err = gen_close_iter(yf);
            gen->gi_frame_state = state;
            Py_DECREF(yf);
            if (err < 0)
                return gen_send_ex(gen, Py_None, 1, 0);
            goto throw_here;
        }
        PyThreadState *tstate = _PyThreadState_GET();
        assert(tstate != NULL);
        if (PyGen_CheckExact(yf) || PyCoro_CheckExact(yf)) {
            /* `yf` is a generator or a coroutine. */

            /* Link frame into the stack to enable complete backtraces. */
            /* XXX We should probably be updating the current frame somewhere in
               ceval.c. */
            _PyInterpreterFrame *prev = tstate->current_frame;
            frame->previous = prev;
            tstate->current_frame = frame;
            /* Close the generator that we are currently iterating with
               'yield from' or awaiting on with 'await'. */
            PyFrameState state = gen->gi_frame_state;
            gen->gi_frame_state = FRAME_EXECUTING;
            ret = _gen_throw((PyGenObject *)yf, close_on_genexit,
                             typ, val, tb);
            gen->gi_frame_state = state;
            tstate->current_frame = prev;
            frame->previous = NULL;
        } else {
            /* `yf` is an iterator or a coroutine-like object. */
            PyObject *meth;
            if (PyObject_GetOptionalAttr(yf, &_Py_ID(throw), &meth) < 0) {
                Py_DECREF(yf);
                return NULL;
            }
            if (meth == NULL) {
                Py_DECREF(yf);
                goto throw_here;
            }

            _PyInterpreterFrame *prev = tstate->current_frame;
            frame->previous = prev;
            tstate->current_frame = frame;
            PyFrameState state = gen->gi_frame_state;
            gen->gi_frame_state = FRAME_EXECUTING;
            ret = PyObject_CallFunctionObjArgs(meth, typ, val, tb, NULL);
            gen->gi_frame_state = state;
            tstate->current_frame = prev;
            frame->previous = NULL;
            Py_DECREF(meth);
        }
        Py_DECREF(yf);
        if (!ret) {
            ret = gen_send_ex(gen, Py_None, 1, 0);
        }
        return ret;
    }

throw_here:
    /* First, check the traceback argument, replacing None with
       NULL. */
    if (tb == Py_None) {
        tb = NULL;
    }
    else if (tb != NULL && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "throw() third argument must be a traceback object");
        return NULL;
    }

    Py_INCREF(typ);
    Py_XINCREF(val);
    Py_XINCREF(tb);

    if (PyExceptionClass_Check(typ))
        PyErr_NormalizeException(&typ, &val, &tb);

    else if (PyExceptionInstance_Check(typ)) {
        /* Raising an instance.  The value should be a dummy. */
        if (val && val != Py_None) {
            PyErr_SetString(PyExc_TypeError,
              "instance exception may not have a separate value");
            goto failed_throw;
        }
        else {
            /* Normalize to raise <class>, <instance> */
            Py_XSETREF(val, typ);
            typ = Py_NewRef(PyExceptionInstance_Class(typ));

            if (tb == NULL)
                /* Returns NULL if there's no traceback */
                tb = PyException_GetTraceback(val);
        }
    }
    else {
        /* Not something you can raise.  throw() fails. */
        PyErr_Format(PyExc_TypeError,
                     "exceptions must be classes or instances "
                     "deriving from BaseException, not %s",
                     Py_TYPE(typ)->tp_name);
            goto failed_throw;
    }

    PyErr_Restore(typ, val, tb);
    return gen_send_ex(gen, Py_None, 1, 0);

failed_throw:
    /* Didn't use our arguments, so restore their original refcounts */
    Py_DECREF(typ);
    Py_XDECREF(val);
    Py_XDECREF(tb);
    return NULL;
}


static PyObject *
gen_throw(PyObject *op, PyObject *const *args, Py_ssize_t nargs)
{
    PyGenObject *gen = _PyGen_CAST(op);
    PyObject *typ;
    PyObject *tb = NULL;
    PyObject *val = NULL;

    if (!_PyArg_CheckPositional("throw", nargs, 1, 3)) {
        return NULL;
    }
    if (nargs > 1) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                            "the (type, exc, tb) signature of throw() is deprecated, "
                            "use the single-arg signature instead.",
                            1) < 0) {
            return NULL;
        }
    }
    typ = args[0];
    if (nargs == 3) {
        val = args[1];
        tb = args[2];
    }
    else if (nargs == 2) {
        val = args[1];
    }
    return _gen_throw(gen, 1, typ, val, tb);
}