from typing import Iterator


iterator: Iterator = iter([1, 2, 3, 4, 5])
print(iterator.__next__())
print(iterator.__next__())

print(iterator.__previous__())