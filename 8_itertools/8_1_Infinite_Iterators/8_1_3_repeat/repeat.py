from typing import Generator, Any


def repeat(obj: Any, times: int=None) -> Generator:
    if times is None:
        while True:
            yield obj
    else:
        for _ in range(times):
            yield obj