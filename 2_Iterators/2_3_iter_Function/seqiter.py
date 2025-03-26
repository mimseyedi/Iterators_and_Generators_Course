from typing import Any, Iterator, Sequence


class SeqIter:
    def __init__(self, sequence: Sequence) -> None:
        self.sequence = sequence
        self.index = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        try:
            value = self.sequence.__getitem__(self.index)
        except IndexError:
            raise StopIteration from None
        else:
            self.index += 1
            return value