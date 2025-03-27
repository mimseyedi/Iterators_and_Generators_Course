from itertools import batched


for row in batched(range(1, 10), 3):
    print(row)