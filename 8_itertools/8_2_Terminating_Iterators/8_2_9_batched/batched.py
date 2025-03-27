from typing import Iterable, Generator
from itertools import islice


def batched(iterable: Iterable, n: int) -> Generator:
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch