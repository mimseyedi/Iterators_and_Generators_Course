import asyncio
from typing import Generator
from contextlib import suppress


class GenStatus:
    def __init__(self, gen: Generator) -> None:
        self.gen = self._target(gen)

    async def is_running(self) -> bool:
        return self.gen.ag_running

    async def is_suspended(self) -> bool:
        return self.gen.ag_suspended

    async def is_closed(self) -> bool:
        return True if self.gen.ag_frame is None else False

    @staticmethod
    async def _target(gen) -> Generator:
        for x in gen:
            await asyncio.sleep(1)
            yield x

    async def _pnv(self) -> None:
        print(f"- Received value: '{await anext(self.gen)}'")

    async def _get_status(self) -> None:
        if await self.is_running():
            print("* Status: Running")
        elif await self.is_suspended():
            print("* Status: Suspended")
        elif await self.is_closed():
            print("* Status: Closed")

    async def monitor(self) -> None:
        print("* Status: The Generator was created")

        with suppress(StopAsyncIteration):
            while True:
                task = asyncio.create_task(self._pnv())
                print("- Request the next value")
                print("* Status: Running")
                await task
                await self._get_status()

        try:
            await anext(self.gen)
        except StopAsyncIteration:
            print("- StopIteration happened!")
            await self._get_status()