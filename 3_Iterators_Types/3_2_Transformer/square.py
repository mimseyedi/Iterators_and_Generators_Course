from typing import Sequence, Iterator


class SquareIterator:
    def __init__(self, sequence: Sequence[int]) -> None:
        self.sequence = sequence
        self.index = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.index < len(self.sequence):
            result = self.sequence[self.index] ** 2
            self.index += 1
            return result
        raise StopIteration