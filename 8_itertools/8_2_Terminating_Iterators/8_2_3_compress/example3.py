from itertools import compress


print(list(compress([1, 2, 6, 3, 7, 9], [0, 0, 1, 0, 1, 1])))
print(list(filter(lambda x: x > 5, [1, 2, 6, 3, 7, 9])))