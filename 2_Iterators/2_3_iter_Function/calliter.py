from typing import Any, Iterator, Callable


class CallIter:
    def __init__(self, callable_: Callable, sentinel: Any) -> None:
        self.callable = callable_
        self.sentinel = sentinel
        self.exhausted = False

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self.exhausted:
            raise StopIteration
        value = self.callable()
        if value == self.sentinel:
            self.exhausted = True
            raise StopIteration
        return value