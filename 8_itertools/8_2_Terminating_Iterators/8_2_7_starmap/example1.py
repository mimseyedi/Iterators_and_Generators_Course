from typing import Iterator
from itertools import starmap


powers: Iterator = starmap(pow, ((2, 3), (3, 2), (5, 2), (10, 3)))

for x in powers:
    print(x)