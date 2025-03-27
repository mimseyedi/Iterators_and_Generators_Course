from typing import Generator


def sub_generator() -> Generator:
    print("We're inside The Sub-Generator")
    value = yield 2
    print("Received", value)
    return 4


def main_generator() -> Generator:
    yield 1
    retval = yield from sub_generator()
    print("Returned", retval)
    yield 5


main_gen: Generator = main_generator()
print(next(main_gen))
print(next(main_gen))
print(main_gen.send(3))