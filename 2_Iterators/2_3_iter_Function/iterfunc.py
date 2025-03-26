from typing import (
    Iterable,
    Iterator,
    Sequence,
    Callable,
)
from seqiter import SeqIter
from calliter import CallIter


def iter_(obj: Iterable | Callable, sentinel=None) -> Iterator:
    if sentinel is None:
        return get_iter(obj)
    if callable(obj):
        return CallIter(obj, sentinel)
    raise TypeError("iter(v, w): v must be callable")


def get_iter(obj: Iterable | Sequence) -> Iterator:
    try:
        it = obj.__iter__()
    except AttributeError:
        if hasattr(obj, '__getitem__'):
            return SeqIter(obj)
        raise TypeError(
            "object is not iterable"
        ) from None
    else:
        if isinstance(it, Iterator):
            return it
        raise TypeError("__iter__() returned non-iterator")