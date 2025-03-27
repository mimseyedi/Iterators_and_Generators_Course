from typing import Generator
from pathlib import Path


def read(path: Path) -> Generator:
    with open(path) as file:
        for lineno, line in enumerate(file, start=1):
            yield path.name, lineno, line.strip()


def search(*files, target: str) -> tuple:
    generators: list[Generator] = [
        read(file) for file in files
    ]
    try:
        closed_gen = 0
        while closed_gen < len(generators):
            for gen in generators:
                try:
                    file, lineno, line = next(gen)
                    if line == target:
                        return file, lineno, line
                except StopIteration:
                    closed_gen += 1
        else:
            return tuple()
    finally:
        for gen in generators:
            gen.close()
        print("All generators closed.")


filenames: tuple = (
    Path("file1.txt"),
    Path("file2.txt"),
    Path("file3.txt"),
)

print(search(*filenames, target="Python"))