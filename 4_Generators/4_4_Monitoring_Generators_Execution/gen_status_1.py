import time
from typing import Generator
from threading import Thread


def sleepy_generator(delay: int) -> Generator:
    for x in ("A", "B", "C"):
        time.sleep(delay)
        yield x


def print_next_value(gen: Generator) -> None:
    print(f"- Received value: '{next(gen)}'")


def is_running(gen: Generator) -> bool:
    return gen.gi_running


def is_suspended(gen: Generator) -> bool:
    return gen.gi_suspended


def is_exhausted(gen: Generator) -> bool:
    return True if gen.gi_frame is None else False


def get_status(gen: Generator) -> None:
    if is_running(gen):
        print("* Status: Running")
    elif is_suspended(gen):
        print("* Status: Suspended")
    elif is_exhausted(gen):
        print("* Status: Exhausted")


def main():
    gen = sleepy_generator(1)
    print("* Status: The Generator was created")

    for _ in range(3):
        thread = Thread(target=print_next_value, args=(gen,))
        thread.start()
        print("- Request the next value")
        get_status(gen)
        thread.join()
        get_status(gen)
    else:
        try:
            print("- Request the next value")
            next(gen)
        except StopIteration:
            print("- StopIteration happened!")
            get_status(gen)


if __name__ == '__main__':
    main()
