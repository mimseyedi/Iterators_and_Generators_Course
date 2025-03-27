// https://github.com/python/cpython/blob/main/Objects/genobject.c#L190


static PySendResult
gen_send_ex2(PyGenObject *gen, PyObject *arg, PyObject **presult,
             int exc, int closing)
{
    PyThreadState *tstate = _PyThreadState_GET();
    _PyInterpreterFrame *frame = &gen->gi_iframe;

    *presult = NULL;
    if (gen->gi_frame_state == FRAME_CREATED && arg && arg != Py_None) {
        const char *msg = "can't send non-None value to a "
                            "just-started generator";
        if (PyCoro_CheckExact(gen)) {
            msg = NON_INIT_CORO_MSG;
        }
        else if (PyAsyncGen_CheckExact(gen)) {
            msg = "can't send non-None value to a "
                    "just-started async generator";
        }
        PyErr_SetString(PyExc_TypeError, msg);
        return PYGEN_ERROR;
    }
    if (gen->gi_frame_state == FRAME_EXECUTING) {
        const char *msg = "generator already executing";
        if (PyCoro_CheckExact(gen)) {
            msg = "coroutine already executing";
        }
        else if (PyAsyncGen_CheckExact(gen)) {
            msg = "async generator already executing";
        }
        PyErr_SetString(PyExc_ValueError, msg);
        return PYGEN_ERROR;
    }
    if (FRAME_STATE_FINISHED(gen->gi_frame_state)) {
        if (PyCoro_CheckExact(gen) && !closing) {
            /* `gen` is an exhausted coroutine: raise an error,
               except when called from gen_close(), which should
               always be a silent method. */
            PyErr_SetString(
                PyExc_RuntimeError,
                "cannot reuse already awaited coroutine");
        }
        else if (arg && !exc) {
            /* `gen` is an exhausted generator:
               only return value if called from send(). */
            *presult = Py_NewRef(Py_None);
            return PYGEN_RETURN;
        }
        return PYGEN_ERROR;
    }

    assert((gen->gi_frame_state == FRAME_CREATED) ||
           FRAME_STATE_SUSPENDED(gen->gi_frame_state));

    /* Push arg onto the frame's value stack */
    PyObject *arg_obj = arg ? arg : Py_None;
    _PyFrame_StackPush(frame, PyStackRef_FromPyObjectNew(arg_obj));

    _PyErr_StackItem *prev_exc_info = tstate->exc_info;
    gen->gi_exc_state.previous_item = prev_exc_info;
    tstate->exc_info = &gen->gi_exc_state;

    if (exc) {
        assert(_PyErr_Occurred(tstate));
        _PyErr_ChainStackItem();
    }

    gen->gi_frame_state = FRAME_EXECUTING;
    EVAL_CALL_STAT_INC(EVAL_CALL_GENERATOR);
    PyObject *result = _PyEval_EvalFrame(tstate, frame, exc);
    assert(tstate->exc_info == prev_exc_info);
    assert(gen->gi_exc_state.previous_item == NULL);
    assert(gen->gi_frame_state != FRAME_EXECUTING);
    assert(frame->previous == NULL);

    /* If the generator just returned (as opposed to yielding), signal
     * that the generator is exhausted. */
    if (result) {
        if (FRAME_STATE_SUSPENDED(gen->gi_frame_state)) {
            *presult = result;
            return PYGEN_NEXT;
        }
        assert(result == Py_None || !PyAsyncGen_CheckExact(gen));
        if (result == Py_None && !PyAsyncGen_CheckExact(gen) && !arg) {
            /* Return NULL if called by gen_iternext() */
            Py_CLEAR(result);
        }
    }
    else {
        assert(!PyErr_ExceptionMatches(PyExc_StopIteration));
        assert(!PyAsyncGen_CheckExact(gen) ||
            !PyErr_ExceptionMatches(PyExc_StopAsyncIteration));
    }

    assert(gen->gi_exc_state.exc_value == NULL);
    assert(gen->gi_frame_state == FRAME_CLEARED);
    *presult = result;
    return result ? PYGEN_RETURN : PYGEN_ERROR;
}

static PySendResult
PyGen_am_send(PyObject *self, PyObject *arg, PyObject **result)
{
    PyGenObject *gen = _PyGen_CAST(self);
    return gen_send_ex2(gen, arg, result, 0, 0);
}

static PyObject *
gen_send_ex(PyGenObject *gen, PyObject *arg, int exc, int closing)
{
    PyObject *result;
    if (gen_send_ex2(gen, arg, &result, exc, closing) == PYGEN_RETURN) {
        if (PyAsyncGen_CheckExact(gen)) {
            assert(result == Py_None);
            PyErr_SetNone(PyExc_StopAsyncIteration);
        }
        else if (result == Py_None) {
            PyErr_SetNone(PyExc_StopIteration);
        }
        else {
            _PyGen_SetStopIterationValue(result);
        }
        Py_CLEAR(result);
    }
    return result;
}

PyDoc_STRVAR(send_doc,
"send(arg) -> send 'arg' into generator,\n\
return next yielded value or raise StopIteration.");

static PyObject *
gen_send(PyObject *gen, PyObject *arg)
{
    return gen_send_ex((PyGenObject*)gen, arg, 0, 0);
}