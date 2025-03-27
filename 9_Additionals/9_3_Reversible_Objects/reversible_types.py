import builtins
from collections.abc import Reversible


def is_reversible(obj: ...) -> bool:
    if not isinstance(obj, type):
        return False
    return issubclass(obj, Reversible)


for key, value in vars(builtins).items():
    if is_reversible(value):
        print(key)