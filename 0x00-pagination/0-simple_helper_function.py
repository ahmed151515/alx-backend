#!/usr/bin/env python3
"""solve task"""


def index_range(page: int, page_size: int):
    s = (page - 1) * page_size
    return (s, s + page_size)
