#!/usr/bin/env python3
"""
    Complex types - string and int/float to tuple
"""
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Returns a tuple.
    """
    return (k, v**2)
