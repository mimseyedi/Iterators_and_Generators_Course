from itertools import repeat


for number in map(pow, range(10), repeat(2)):
    print(number)