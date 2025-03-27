from itertools import takewhile


for number in takewhile(lambda x: x < 5, [1, 3, 7, 2, 0, 9]):
    print(number)