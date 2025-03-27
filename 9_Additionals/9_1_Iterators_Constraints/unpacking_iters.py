from typing import Iterator


iterator: Iterator = iter([1, 2, 3])

a, b, c = iterator
print(a, b, c)

print(next(iterator))