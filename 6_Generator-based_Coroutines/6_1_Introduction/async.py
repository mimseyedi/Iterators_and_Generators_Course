import asyncio


async def a():
    await asyncio.sleep(1)
    print("Function 'A' executed!\n")


async def b():
    await asyncio.sleep(1)
    print("Function 'B' executed!\n")


async def main():
    await asyncio.gather(
        a(),
        b(),
    )


asyncio.run(main())