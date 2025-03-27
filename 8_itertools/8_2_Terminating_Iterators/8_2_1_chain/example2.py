from typing import Iterator, Generator
from itertools import chain


def read(filename: str) -> Generator:
    with open(filename) as f:
        for l in f:
            yield l


filenames = ['file1.txt', 'file2.txt', 'file3.txt']

combined_lines: Iterator = chain(*[read(fn) for fn in filenames])

for line in combined_lines:
    print(line)
