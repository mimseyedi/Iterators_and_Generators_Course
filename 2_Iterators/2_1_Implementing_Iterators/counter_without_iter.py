from collections.abc import Iterator


class Counter(Iterator):
    def __init__(self, roof: int) -> None:
        self.roof: int = roof
        self.current: int = 0

    def __next__(self) -> int:
        if self.current < self.roof:
            c: int = self.current
            self.current += 1
            return c
        else:
            raise StopIteration