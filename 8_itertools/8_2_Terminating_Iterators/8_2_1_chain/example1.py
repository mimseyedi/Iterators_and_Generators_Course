from typing import Iterator
from itertools import chain


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined: Iterator = chain(list1, list2, list3)

for item in combined:
    print(item)
