from typing import Generator


def counter(roof: int) -> Generator:
    for x in range(roof):
        yield x


# -> Initializing
gen: Generator = counter(5)

for _ in gen:
    print(gen.gi_frame.f_locals['x'])