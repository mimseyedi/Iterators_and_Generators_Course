from typing import Iterator, Any


class Counter:
    def __init__(self, roof: int) -> None:
        self.roof = roof
        self.current = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self.current < self.roof:
            result = self.current
            self.current += 1
            return result
        raise StopIteration

    def __reversed__(self):
        counter = self.roof
        while counter > 0:
            yield counter
            counter -= 1