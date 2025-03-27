from typing import Generator


def chain(*iterables) -> Generator:
    for iterable in iterables:
        yield from iterable