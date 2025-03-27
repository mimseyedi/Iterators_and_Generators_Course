from pathlib import Path


# A subroutine:
def read_file(file_path: Path) -> str:
    with open(file_path) as file:
        data: str = file.read()
    return data