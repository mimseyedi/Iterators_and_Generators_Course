from itertools import dropwhile


for item in dropwhile(lambda x: x < 5, [1, 3, 6, 2, 7, 0]):
    print(item)