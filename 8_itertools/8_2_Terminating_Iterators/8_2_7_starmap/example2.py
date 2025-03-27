from itertools import starmap


matrix1 = [
    [1, 2, 3],     # row1
    [4, 5, 6],     # row2
]

matrix2 = [
    [7 , 8 , 9 ],  # row1
    [10, 11, 12],  # row2
]

for row1, row2 in zip(matrix1, matrix2):
    print(list(starmap(lambda x, y: x + y, zip(row1, row2))))