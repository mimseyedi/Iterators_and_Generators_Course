from typing import Iterable
from sys import getsizeof


def get_roots(iterable: Iterable[int]) -> list[float]:
    roots_list = []
    for item in iterable:
        roots_list.append(item ** 0.5)
    return roots_list


roots: list[float] = get_roots(range(1, 10_000))
print(getsizeof(roots), 'bytes')


# Using pympler
from pympler import asizeof
print(asizeof.asizeof(roots), 'bytes')