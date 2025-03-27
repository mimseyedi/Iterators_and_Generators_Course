from typing import Generator


def compress(iterable, selectors) -> Generator:
    for element, selector in zip(iterable, selectors):
        if selector:
            yield element