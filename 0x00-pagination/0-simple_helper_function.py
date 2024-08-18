#!/usr/bin/env python3
"""solve task"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """function to solve task"""
    s = (page - 1) * page_size
    return (s, s + page_size)
