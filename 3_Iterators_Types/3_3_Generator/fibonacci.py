from typing import Iterator


class Fibonacci:
    def __init__(self, n: int) -> None:
        self.n = n
        self.a = 0
        self.b = 1
        self.counter = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.counter < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.counter += 1
            return self.a
        raise StopIteration