from typing import Iterable, Generator
from pathlib import Path


def readlogs(logs_file: Path) -> Generator:
    with open(logs_file) as file:
        for log in file:
            datetime, level, message = map(str.strip, log.split('-'))
            yield datetime, level, message


def find_error(logs: Iterable) -> Generator:
    for log in logs:
        level = log[1]
        if level == 'ERROR':
            yield log


def get_datetime(logs: Iterable) -> Generator:
    for log in logs:
        datetime = log[0]
        yield datetime


logsfile = Path("logs.txt")

for dt in get_datetime(find_error(readlogs(logsfile))):
    print(dt)