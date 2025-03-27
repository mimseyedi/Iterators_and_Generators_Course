from typing import Generator, Iterable


def classic_generator(iterable: Iterable) -> Generator:
    for item in iterable:
        yield item
    # or:
    # yield from iterable