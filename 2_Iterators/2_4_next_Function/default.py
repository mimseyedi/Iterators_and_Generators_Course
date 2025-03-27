from typing import Iterator


names: tuple = (
    'Mohammad',
    'Farhad',
    'Goli',
)

it: Iterator = iter(names)

print(next(it))
print(next(it))
print(next(it))
print(next(it, 'Nobody!'))

