from typing import Generator, Callable, Iterable


def starmap(func: Callable, iterable: Iterable) -> Generator:
    for args in iterable:
        yield func(*args)