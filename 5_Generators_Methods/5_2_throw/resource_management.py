from typing import Generator
from pathlib import Path


def readfile(path: Path) -> Generator:
    file = open(path)
    try:
        for line in file:
            yield line.strip()
    except ValueError:
        print("- ERROR: The file is corrupted!")
    finally:
        file.close()
    yield "- MESSAGE: The file is securely closed."


gen: Generator = readfile(Path('names.txt'))

for x in gen:
    print(x)
    if x == 'NULL':
        print(gen.throw(ValueError))