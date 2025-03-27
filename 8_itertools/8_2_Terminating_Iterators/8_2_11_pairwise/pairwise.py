from typing import Iterable, Generator


def pairwise(iterable: Iterable) -> Generator:
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b