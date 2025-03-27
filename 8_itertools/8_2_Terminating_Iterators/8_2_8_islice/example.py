from itertools import islice


for element in islice(range(11), None, None, 2):
    print(element)