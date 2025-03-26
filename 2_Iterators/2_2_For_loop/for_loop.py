from typing import Iterator, Iterable


iterable: Iterable = [1, 2, 3, 4, 5]

iterator: Iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break