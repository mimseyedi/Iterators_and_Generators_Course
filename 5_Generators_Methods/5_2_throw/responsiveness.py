from typing import Iterable, Iterator, Generator


def iterate(iterable: Iterable) -> Generator:
    try:
        for item in iterable:
            yield item
    except ValueError:
        new_iterable = yield "- Send a new iterable"
        print("Received iterable:", new_iterable)
        yield iterate(new_iterable)


iter_iterables: Iterator = iter(
    [
        [1, 2, None, 3 ],
        ['a', None, 'b'],
        ['x', 'y', 'z' ],
    ]
)

gen: Generator = iterate(next(iter_iterables))

while True:
    try:
        nextval = next(gen)
        print(nextval)
        if nextval is None:
            print(gen.throw(ValueError))
            gen = gen.send(next(iter_iterables))
    except StopIteration:
        break