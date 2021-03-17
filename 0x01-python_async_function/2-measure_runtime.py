#!/usr/bin/env python3
"""
    import the previous file. Asynchronous routine
    that takes two int arguments
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        returns total time / n. Your function should return a float.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    start_time = time.time() - start_time
    return start_time / n
