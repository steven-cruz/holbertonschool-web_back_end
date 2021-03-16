#!/usr/bin/env python3
"""
    takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        returns a function that multiplies a float by multiplier
    """
    def m_m(i: float):
        """
            float for multiplier
        """
        return i * multiplier
    return m_m
