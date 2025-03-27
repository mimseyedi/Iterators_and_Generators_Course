from typing import Generator, Any


def gnext(gen: Generator) -> Any:
    return gen.send(None)