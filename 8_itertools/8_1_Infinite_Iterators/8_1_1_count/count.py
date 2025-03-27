from typing import Generator


def count(start=0, step=1) -> Generator:
    n = start
    while True:
        yield n
        n += step