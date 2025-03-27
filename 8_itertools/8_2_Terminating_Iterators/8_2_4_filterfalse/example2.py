from itertools import filterfalse


for x in filterfalse(None, [1, 0, True, "", [], False]):
    print(x)