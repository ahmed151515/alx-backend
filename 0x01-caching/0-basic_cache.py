#!/usr/bin/env python3
""" BaseCache module
"""

from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """do task ffkgkdfgdf"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
