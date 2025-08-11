from typing import Generator, Any


def gennext(gen: Generator) -> Any:
    return gen.send(None)


gen: Generator = (x ** 2 for x in range(1, 4))
print(gennext(gen))
print(gennext(gen))
print(gennext(gen))
print(gennext(gen))