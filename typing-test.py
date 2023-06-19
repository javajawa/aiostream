from __future__ import annotations

from collections.abc import AsyncIterable
from typing import reveal_type

import asyncio
import random
import aiostream


async def random_delay_counter() -> AsyncIterable[int]:
    i = 0
    while i < 10:
        i += 1
        await asyncio.sleep(random.randint(20, 100) / 100)
        yield i


async def main() -> None:
    merged = aiostream.stream.merge(random_delay_counter(), random_delay_counter())

    async with merged.stream() as streamer:
        async for i in streamer:
            print(i.real, i.imag)

    print("Confirming 'range' has raw but no pipe (one type error expected).")
    reveal_type(aiostream.stream.create.range.raw)
    reveal_type(aiostream.stream.create.range.pipe)


asyncio.run(main())
