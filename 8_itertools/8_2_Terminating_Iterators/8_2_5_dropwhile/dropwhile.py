from typing import Iterable, Callable, Generator


def dropwhile(predicate: Callable, iterable: Iterable) -> Generator:
    iterator = iter(iterable)
    for element in iterator:
        if not predicate(element):
            yield element
            break
    for element in iterator:
        yield element