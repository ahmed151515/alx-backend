#!/usr/bin/env python3
"""solve task"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """fun"""
    s = (page - 1) * page_size
    return (1, s + page_size)
