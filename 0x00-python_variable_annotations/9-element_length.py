#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values
with the appropriate types
"""
from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        length of element
    """
    return [(i, len(i)) for i in lst]
