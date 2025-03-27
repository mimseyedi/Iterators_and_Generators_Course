from typing import Generator


square_gen: Generator = (
    number ** 2 for number in range(1, 11) if number % 2 == 0
)