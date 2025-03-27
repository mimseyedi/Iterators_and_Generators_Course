from itertools import zip_longest


numbers: list = [1, 2]
names:   list = ['Mohammad', 'Farhad', 'Goli']


print(list(zip_longest(numbers, names, fillvalue='?')))