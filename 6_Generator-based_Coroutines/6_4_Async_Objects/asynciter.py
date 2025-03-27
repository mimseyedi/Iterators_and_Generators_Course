import asyncio
from typing import AsyncIterator


class AsyncCounter:
    def __init__(self, roof: int) -> None:
        self.roof = roof
        self.current: int = 0

    def __aiter__(self) -> AsyncIterator:
        return self

    async def __anext__(self) -> int:
        if self.current < self.roof:
            c: int = self.current
            self.current += 1
            await asyncio.sleep(1)
            return c
        raise StopAsyncIteration