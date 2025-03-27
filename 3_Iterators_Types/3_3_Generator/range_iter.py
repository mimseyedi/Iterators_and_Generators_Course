from typing import Iterator


class Range:
    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.current < self.stop:
            c: int = self.current
            self.current += self.step
            return c
        raise StopIteration