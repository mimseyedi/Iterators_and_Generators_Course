from itertools import islice
from typing import Iterator


iterator: Iterator = iter([1, 2, 3, 4, 5])

for x in islice(iterator, 1, 4):
    print(x)

print(next(iterator))