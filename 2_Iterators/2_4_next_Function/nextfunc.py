from typing import Iterator, Any


def next_(it: Iterator, default=None) -> Any:
    if not isinstance(it, Iterator):
        raise TypeError(
            f"'{type(it).__name__}' object is not an iterator"
        )
    try:
        return it.__next__()
    except StopIteration:
        if default is not None:
            return default
        raise