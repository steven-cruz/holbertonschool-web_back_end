#!/usr/bin/env python3
"""
    type annotations are added to the function
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        Return key if it exists, otherwise return default
    """
    if key in dct:
        return dct[key]
    else:
        return default
