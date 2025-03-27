from typing import Iterable, Generator


def cycle(iterable: Iterable) -> Generator:
    saved = []
    for element in iterable:
        yield element
        saved.append(element)

    while saved:
        for element in saved:
            yield element