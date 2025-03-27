from typing import Generator


def counting_1_and_2() -> Generator:
    yield 1
    yield 2


def counting_3_and_4() -> Generator:
    yield 3
    yield 4


def counting_to_6() -> Generator:
    yield from counting_1_and_2()
    yield from counting_3_and_4()
    yield 5
    yield 6


main_gen = counting_to_6()

for x in main_gen:
    sub_gen = main_gen.gi_yieldfrom
    if sub_gen is not None:
        print(f"- {sub_gen.__name__}")
    else:
        print(f"- {main_gen.__name__}")

    print("\tYielded value:", x)