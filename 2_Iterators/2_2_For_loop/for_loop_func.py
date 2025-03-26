from typing import Iterator, Iterable, Callable


def for_loop(iterable: Iterable, func: Callable) -> None:
    iterator: Iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)


for_loop([1, 2, 3, 4, 5], print)