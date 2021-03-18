#!/usr/bin/env python3
"""
    compile 10 random numbers using an asynchronous comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        returns the 10 random numbers
    """
    return [val async for val in async_generator()]
