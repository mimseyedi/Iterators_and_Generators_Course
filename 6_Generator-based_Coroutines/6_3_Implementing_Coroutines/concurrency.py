import time
from typing import Generator


def create_task(name: str, steps: int) -> Generator:
    for step in range(1, steps + 1):
        print(f"{name}: step {step}/{steps}")
        yield time.sleep(1)
    return f"{name}: DONE."


def run(*tasks) -> None:
    lt = list(tasks)

    while len(lt):
        for index, task in enumerate(lt):
            try:
                next(task)
            except StopIteration as returned:
                print(returned.value)
                lt.pop(index)

    print("[There is no task to run!]")


def main():
    task_a = create_task("A", 3)
    task_b = create_task("B", 7)
    task_c = create_task("C", 5)

    run(task_a, task_b, task_c)


if __name__ == '__main__':
    main()