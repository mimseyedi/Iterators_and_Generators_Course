from typing import Generator


def fibonacci(n: int) -> Generator:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b