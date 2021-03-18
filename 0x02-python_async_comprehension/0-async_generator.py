#!/usr/bin/env python3
"""
    coroutine that is repeated 10 times, each time it waits asynchronously
    for 1 second, then produces a random number between 0 and 10
"""
import asyncio
import random
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        then produce a random number between
        0 and 10 with the random module
    """
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
