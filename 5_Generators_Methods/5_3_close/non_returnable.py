from typing import Generator


def simple_generator() -> Generator:
    yield 1
    yield 2
    yield 3


gen: Generator = simple_generator()

print(next(gen))

try:
    # gen.close()
    gen.throw(GeneratorExit)
except GeneratorExit:
    print("Returned GeneratorExit, received.")

print("frame:", gen.gi_frame)

