from typing import Generator


def simple_generator() -> Generator:
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator is being closed with GeneratorExit...")
        yield 0


gen: Generator = simple_generator()

print(next(gen))

gen.close()
# print(gen.throw(GeneratorExit))