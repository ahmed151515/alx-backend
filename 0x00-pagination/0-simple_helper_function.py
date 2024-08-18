#!/usr/bin/env python3
"""solve task"""
from typing import Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[Union[int, int]]:
    s = (page - 1) * page_size
    return (1, s + page_size)
