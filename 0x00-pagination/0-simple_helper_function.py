#!/usr/bin/env python3
"""
asd
"""


def index_range(page, page_size):
    """
    Returns the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)