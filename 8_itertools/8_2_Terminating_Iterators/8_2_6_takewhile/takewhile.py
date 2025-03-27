from typing import Callable, Iterable, Generator


def takewhile(predicate: Callable, iterable: Iterable) -> Generator:
    for element in iterable:
        if not predicate(element):
            break
        yield element