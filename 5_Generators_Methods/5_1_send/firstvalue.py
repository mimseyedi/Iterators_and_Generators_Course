from typing import Generator


def generator():
    x = yield 1
    print("received:", x)
    yield x


gen: Generator = generator()
print(next(gen))
print(next(gen))