#!/usr/bin/env python3
"""
    Take the code from wait_n and alter it into a new function task_wait_n
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        task_wait_n function
    """
    i: List[float] = []
    for _ in range(n):
        i.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(i)]
