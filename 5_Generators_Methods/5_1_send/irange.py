from typing import Generator


def irange(start: int, stop: int, step: int=1) -> Generator:
    current = start
    while current < stop:
        custom_step = yield current
        if custom_step is not None:
            current += custom_step
            yield current
        else:
            current += step