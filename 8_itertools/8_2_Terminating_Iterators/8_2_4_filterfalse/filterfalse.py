from typing import Iterable, Callable, Generator


def filterfalse(predicate: Callable, iterable: Iterable) -> Generator:
    if predicate is None:
        predicate = bool
    for element in iterable:
        if not predicate(element):
            yield element