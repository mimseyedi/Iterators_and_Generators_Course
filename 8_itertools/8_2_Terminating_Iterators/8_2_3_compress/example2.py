from itertools import compress


def get_column(data: tuple[list], column: int) -> list:
    return [row[column] for row in data]


employees: tuple = (
    ['Akram', 15_000_000, 'Design'     , 5 , False],
    ['Saman', 10_000_000, 'Testing'    , 7 , True ],
    ['Fazel', 12_000_000, 'HR'         , 10, False],
    ['Sara' , 10_000_000, 'Development', 4 , True ],
    ['Amin' , 14_000_000, 'DevOps'     , 9 , True ],
)

names: list[str] = get_column(employees, 0)
is_married: list[bool] = get_column(employees, -1)

for qualified_employees in compress(names, is_married):
    print(qualified_employees)