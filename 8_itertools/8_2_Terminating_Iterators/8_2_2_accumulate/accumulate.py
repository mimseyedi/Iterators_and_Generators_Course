from typing import Iterable, Callable, Generator
from operator import add


def accumulate(
    iterable: Iterable, func: Callable=add, *, initial: int|None=None,
) -> Generator:

    iterator = iter(iterable)
    total = initial

    if initial is None:
        try:
            total = next(iterator)
        except StopIteration:
            return
    yield total

    for element in iterator:
        total = func(total, element)
        yield total