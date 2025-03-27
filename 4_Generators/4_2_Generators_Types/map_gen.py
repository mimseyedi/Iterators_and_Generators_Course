from typing import Iterable, Generator, Callable


def map_gen(func: Callable, iterable: Iterable) -> Generator:
    for item in iterable:
        yield func(item)