from typing import Sequence, Any, Iterator


def reversed_(obj: Any) -> Iterator | Any:
    if hasattr(obj, '__reversed__'):
        return obj.__reversed__()
    if is_sequence(obj):
        return ReverseIterator(obj)
    raise TypeError(
        f"'{type(obj).__name__}' object is not reversible"
    )


def is_sequence(obj: Any) -> bool:
    if hasattr(obj, '__getitem__') and hasattr(obj, '__len__'):
        return True
    return False


class ReverseIterator:
    def __init__(self, seq: Sequence) -> None:
        self.seq = seq
        self.index = len(seq) - 1

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self.index >= 0:
            item = self.seq.__getitem__(self.index)
            self.index -= 1
            return item
        raise StopIteration

    def __str__(self) -> str:
        return f"reversed object at {hex(id(self))}"