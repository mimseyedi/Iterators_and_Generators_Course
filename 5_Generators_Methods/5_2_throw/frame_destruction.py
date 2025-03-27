from typing import Generator


def simple_generator() -> Generator:
    yield 1
    yield 2
    yield 3


gen: Generator = simple_generator()

print(next(gen))
try:
    gen.throw(ValueError)
except ValueError:
    pass

print(gen.gi_frame)