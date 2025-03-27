from typing import Iterator
from itertools import count


e: Iterator = count(start=2, step=2)
print([next(e) for _ in range(11)])


o: Iterator = count(start=1, step=2)
print([next(o) for _ in range(11)])