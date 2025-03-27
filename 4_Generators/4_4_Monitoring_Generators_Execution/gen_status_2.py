import time
from typing import Generator
from threading import Thread


GREEN  = '\x1b[32m'
YELLOW = '\x1b[33m'


def echo(value, message=None, color=None, end='\n') -> None:
    print(
        color if color else '',
        message if message else '',
        value,
        '\x1b[0m',
        sep='',
        end=end,
    )


def sleepy_generator(delay: int) -> Generator:
    for x in ("A", "B", "C"):
        time.sleep(delay)
        yield x


def print_next_value(gen: Generator) -> None:
    echo(
        value=f"'{next(gen)}'",
        message="⬤ Received value: ",
        color=YELLOW,
    )


def is_running(gen: Generator) -> bool:
    return gen.gi_running


def is_suspended(gen: Generator) -> bool:
    return gen.gi_suspended


def is_exhausted(gen: Generator) -> bool:
    return True if gen.gi_frame is None else False


def get_status(gen: Generator) -> None:
    echo("─" * 45)
    echo("GENERATOR STATUS:")

    echo("\t├── Running:", end='\t')
    if is_running(gen):
        echo('True\t⬅', color=GREEN)
    else:
        echo('False')

    echo("\t├── Suspended:", end='\t')
    if is_suspended(gen):
        echo('True\t⬅', color=GREEN)
    else:
        echo('False')

    echo("\t└── Exausted:", end='\t')
    if is_exhausted(gen):
        echo('True\t⬅', color=GREEN)
    else:
        echo('False')
    echo("─" * 45)


def main():
    gen: Generator = sleepy_generator(1)
    echo("\n⬤ The Generator was created", color=YELLOW)
    get_status(gen)

    for _ in range(3):
        t1 = Thread(target=print_next_value, args=(gen,))
        t1.start()
        echo("⬤ Request the next value", color=YELLOW)
        get_status(gen)
        t1.join()
        get_status(gen)
    else:
        try:
            echo("⬤ Request the next value", color=YELLOW)
            next(gen)
        except StopIteration:
            echo("⬤ StopIteration happened!", color=YELLOW)
            get_status(gen)


if __name__ == '__main__':
    main()