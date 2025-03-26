from random import randint
from typing import Iterator


def roll():
    return randint(1, 6)


it: Iterator = iter(roll, 6)

for x in it:
    print(x)
else:
    print("6 -> Lucky!")