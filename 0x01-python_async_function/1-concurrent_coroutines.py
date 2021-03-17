#!/usr/bin/env python3
"""
    import the previous file. Asynchronous routine
    that takes two int arguments
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        returns the list of all delays without using sort()
    """
    i: List[float] = []
    for _ in range(n):
        i.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(i)]
