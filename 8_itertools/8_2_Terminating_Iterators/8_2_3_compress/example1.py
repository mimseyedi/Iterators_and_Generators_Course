from itertools import compress


print(list(compress("ABCDEFG", [1, 0, 0, 1, 0, 1, 1])))