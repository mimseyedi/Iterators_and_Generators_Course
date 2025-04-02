from typing import Iterator, Iterable


iterable: Iterable = [1, 2, 3, 4, 5]

iterator: Iterator = iter(iterable)

while value := next(iterator, None):
    print(value)