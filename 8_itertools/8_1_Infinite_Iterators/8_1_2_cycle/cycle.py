from typing import Iterable, Generator


def cycle(iterable: Iterable) -> Generator:
    while True:
        for element in iterable:
            yield element