from typing import Generator


def counter(roof: int) -> Generator:
    c = 0
    while c < roof:
        yield c
        c += 1