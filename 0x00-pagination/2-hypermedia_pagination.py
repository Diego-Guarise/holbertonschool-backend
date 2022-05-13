#!/usr/bin/env python3
"""
asd
"""


import csv
from typing import List
import math


index_range = __import__('0-simple_helper_function').index_range


def index_range(page, page_size):
    """
    Returns the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """
    Class
    """
    file = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Dataset
        """
        if self.__dataset is None:
            with open(self.file) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns data
        """

        assert isinstance(page, int), "AssertionError raised when page \
                                    and/or page_size are not ints"
        assert isinstance(page_size, int), "AssertionError raised when page \
                                    and/or page_size are not ints"
        assert page > 0, "AssertionError raised with negative values"
        assert page_size > 0, "AssertionError raised with negative values"

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:
        """
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 < math.ceil(
                len(self.__dataset) / page_size) else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
