from typing import Generator


def sub_generator() -> Generator:
    yield 1
    yield 2
    return 99


def main_generator() -> Generator:
    yield 0
    retval = yield from sub_generator()
    print("Returned value from Sub-Generator:", retval)
    yield 3


for x in main_generator():
    print(x)