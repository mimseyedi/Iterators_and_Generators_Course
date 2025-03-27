import asyncio
import time
from typing import AsyncGenerator, Generator


async def task(delay: int):
    await asyncio.sleep(delay)
    print("TASK execution, finished!")


def counter(roof: int) -> Generator:
    for x in range(roof):
        time.sleep(1)
        yield x


async def async_counter(roof: int) -> AsyncGenerator:
    for x in range(roof):
        await asyncio.sleep(1)
        yield x


async def async_process():
    async for data in async_counter(3):
        print("Generated data:", data)

    # for data in counter(3):
    #     print("Generated data:", data)


async def main():
    await asyncio.gather(
        task(2),
        async_process(),
    )


asyncio.run(main())