from contextlib import suppress
from typing import Iterator, Iterable, Callable


def for_loop(iterable: Iterable, func: Callable) -> None:
    iterator: Iterator = iter(iterable)
    with suppress(StopIteration):
        while True:
            value = next(iterator)
            func(value)


for_loop([1, 2, 3, 4, 5], print)