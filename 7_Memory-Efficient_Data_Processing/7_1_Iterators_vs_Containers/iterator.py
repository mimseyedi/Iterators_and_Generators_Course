from typing import Iterable, Generator
from pympler import asizeof


def get_roots(iterable: Iterable[int]) -> Generator:
    for item in iterable:
        yield item ** 0.5


roots: Generator = get_roots(range(1, 1_000_000))

print(asizeof.asizeof(roots), 'bytes')

print(asizeof.asizeof(next(roots)), 'bytes')
print(asizeof.asizeof(next(roots)), 'bytes')
print(asizeof.asizeof(next(roots)), 'bytes')