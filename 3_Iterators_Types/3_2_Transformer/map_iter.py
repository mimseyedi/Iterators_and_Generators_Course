from typing import Any, Callable, Iterable, Iterator


class Map:
    def __init__(self, func: Callable, iterable: Iterable) -> None:
        self.func = func
        self.iterator = iter(iterable)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if element := next(self.iterator, None):
            return self.func(element)
        raise StopIteration