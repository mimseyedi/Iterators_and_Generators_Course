import asyncio


async def create_task(name: str, steps: int) -> None:
    for step in range(1, steps + 1):
        print(f"{name}: step {step}/{steps}")
        await asyncio.sleep(1)
    print(f"{name}: DONE")


async def run(*tasks) -> None:
    await asyncio.gather(*tasks)
    print("[There is no task to run!]")


async def main() -> None:
    task_a = create_task("A", 3)
    task_b = create_task("B", 7)
    task_c = create_task("C", 5)

    await run(task_a, task_b, task_c)


asyncio.run(main())