from itertools import filterfalse


def is_even(n: int) -> bool:
    return n % 2 == 0


result = list(filterfalse(is_even, range(10)))
print(result)

