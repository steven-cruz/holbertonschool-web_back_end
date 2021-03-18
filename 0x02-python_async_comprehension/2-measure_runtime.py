#!/usr/bin/env python3
"""
    measure_runtime coroutine that will execute
    async_comprehension four times in parallel using
    asyncio.gather.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        returns the measurement of time and total execution
    """
    s_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - s_time
