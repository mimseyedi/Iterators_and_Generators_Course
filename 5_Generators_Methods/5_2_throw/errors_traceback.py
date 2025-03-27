from typing import Iterable, Generator


def iterate(iterable: Iterable) -> Generator:
    for step, item in enumerate(iterable, start=1):
        try:
            yield item
        except ValueError:
            raise ValueError(f"Problematic value in step '{step}'")



gen: Generator = iterate(
    [1, 2, 3, 4, None, 5, 6, None, 7, 8]
)

for x in gen:
    print(x)
    if x is None:
        # raise ValueError("A None value was found!")
        gen.throw(ValueError, "A None value was found!")
