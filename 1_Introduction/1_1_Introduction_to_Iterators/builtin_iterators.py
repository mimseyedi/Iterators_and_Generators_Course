import builtins
from collections.abc import Iterator


def isiterator(obj: ...) -> bool:
    if not isinstance(obj, type):
        return False
    return issubclass(obj, Iterator)


for key, value in vars(builtins).items():
    if isiterator(value):
        print(key)