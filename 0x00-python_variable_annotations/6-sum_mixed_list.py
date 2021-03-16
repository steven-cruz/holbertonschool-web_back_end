#!/usr/bin/env python3
"""
annotation function that takes a list of integers and floats
and returns the sum as floats
"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the sum as floats
    """
    return sum(mxd_lst)
