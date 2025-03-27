from typing import Iterator
from itertools import cycle


alphabet: Iterator = cycle(map(chr, range(65, 91)))

for _ in range(30):
    print(next(alphabet))
