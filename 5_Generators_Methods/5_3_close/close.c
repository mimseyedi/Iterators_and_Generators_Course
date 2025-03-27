// https://github.com/python/cpython/blob/main/Objects/genobject.c#L385


static PyObject *
gen_close(PyObject *self, PyObject *args)
{
    PyGenObject *gen = _PyGen_CAST(self);

    if (gen->gi_frame_state == FRAME_CREATED) {
        gen->gi_frame_state = FRAME_COMPLETED;
        Py_RETURN_NONE;
    }
    if (FRAME_STATE_FINISHED(gen->gi_frame_state)) {
        Py_RETURN_NONE;
    }

    PyObject *yf = _PyGen_yf(gen);
    int err = 0;
    if (yf) {
        PyFrameState state = gen->gi_frame_state;
        gen->gi_frame_state = FRAME_EXECUTING;
        err = gen_close_iter(yf);
        gen->gi_frame_state = state;
        Py_DECREF(yf);
    }
    _PyInterpreterFrame *frame = &gen->gi_iframe;
    if (is_resume(frame->instr_ptr)) {
        /* We can safely ignore the outermost try block
         * as it is automatically generated to handle
         * StopIteration. */
        int oparg = frame->instr_ptr->op.arg;
        if (oparg & RESUME_OPARG_DEPTH1_MASK) {
            // RESUME after YIELD_VALUE and exception depth is 1
            assert((oparg & RESUME_OPARG_LOCATION_MASK) != RESUME_AT_FUNC_START);
            gen->gi_frame_state = FRAME_COMPLETED;
            gen_clear_frame(gen);
            Py_RETURN_NONE;
        }
    }
    if (err == 0) {
        PyErr_SetNone(PyExc_GeneratorExit);
    }

    PyObject *retval = gen_send_ex(gen, Py_None, 1, 1);
    if (retval) {
        const char *msg = "generator ignored GeneratorExit";
        if (PyCoro_CheckExact(gen)) {
            msg = "coroutine ignored GeneratorExit";
        } else if (PyAsyncGen_CheckExact(gen)) {
            msg = ASYNC_GEN_IGNORED_EXIT_MSG;
        }
        Py_DECREF(retval);
        PyErr_SetString(PyExc_RuntimeError, msg);
        return NULL;
    }
    assert(PyErr_Occurred());

    if (PyErr_ExceptionMatches(PyExc_GeneratorExit)) {
        PyErr_Clear();          /* ignore this error */
        Py_RETURN_NONE;
    }

    /* if the generator returned a value while closing, StopIteration was
     * raised in gen_send_ex() above; retrieve and return the value here */
    if (_PyGen_FetchStopIterationValue(&retval) == 0) {
        return retval;
    }
    return NULL;
}