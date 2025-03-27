from typing import Generator


def range_gen(start: int, stop: int, step: int=1) -> Generator:
    current = start
    while current < stop:
        yield current
        current += step