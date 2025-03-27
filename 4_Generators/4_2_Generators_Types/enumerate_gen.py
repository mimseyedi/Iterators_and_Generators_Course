from typing import Generator, Iterable


def enumerate_gen(iterable: Iterable, *, start: int=0) -> Generator:
    c = start
    for item in iterable:
        yield c, item
        c += 1