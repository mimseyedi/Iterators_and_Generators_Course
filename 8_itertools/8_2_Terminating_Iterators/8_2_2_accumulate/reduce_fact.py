from functools import reduce
from operator import mul


def factorial(n: int) -> int:
    return reduce(mul, range(1, n + 1))


print('5! =', factorial(5))

# 5!
# 1x2  = 2
# 2x3  = 6
# 6x4  = 24
# 24x5 = 120