#!/usr/bin/env python3


def index_range(page, page_size):
    """
        Returns a tuple, containing a starting index
        and a completion index
    """
    return((page_size * (page - 1)), page_size * page)
