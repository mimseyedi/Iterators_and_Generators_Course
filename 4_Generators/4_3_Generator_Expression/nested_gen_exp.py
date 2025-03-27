from typing import Generator


messed_up_tuple: tuple = (
    "543543",
    "Mohammad",
    "123ab",
    "3.....",
    "Maryam",
    "r3b2!@",
    "Goli",
    "Naser",
    "Keyv@n",
)

nested_gen_expr: Generator = (
    name[::-1] for name in (
        item.upper() for item in messed_up_tuple if item.isalpha()
    )
)