from typing import Generator, Sequence


def square(sequence: Sequence) -> Generator:
    for number in sequence:
        yield number ** 2