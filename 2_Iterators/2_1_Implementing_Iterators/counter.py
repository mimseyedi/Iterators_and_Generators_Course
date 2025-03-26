from typing import Iterator


class Counter:
    def __init__(self, roof: int) -> None:
        self.roof: int = roof
        self.current: int = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.current < self.roof:
            c: int = self.current
            self.current += 1
            return c
        else:
            raise StopIteration