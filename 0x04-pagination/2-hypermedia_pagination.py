#!/usr/bin/env python3
""" Simple pagination """

import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            - Use assert to verify that both arguments
            are integers greater than 0.

            - Use index_range to find the correct indexes to paginate
            the dataset correctly and return the appropriate page
            of the dataset (i.e. the correct list of rows).
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0

        pages, page_sizes = index_range(page, page_size)
        csv = []
        if pages >= len(self.dataset()):
            return csv
        csv = self.dataset()
        return csv[pages:page_sizes]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
            returns a dictionary containing the following key-value pairs
        """
        size_all_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < size_all_pages else None
        prev_page = page - 1 if page > 1 else None
        data = {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': size_all_pages}
        return data
