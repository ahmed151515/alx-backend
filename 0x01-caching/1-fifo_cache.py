#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class node:
    def __init__(self, key, value, next) -> None:
        self.key = key
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return self.value


class FIFOCache(BaseCaching):
    """do task ffkgkdfgdf"""

    def __init__(self):
        super().__init__()
        self.front = None
        self.back = None

        self.count = 0

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if self.count >= BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.front.key}")
            del self.cache_data[self.front.key]
            self.front = self.front.next
            nod = node(key, item, None)
            self.back.next = nod
            self.back = nod
            self.cache_data[key] = nod
            self.count -= 1
        else:
            if self.front is None:
                nod = node(key, item, None)
                self.front = nod
                self.back = nod
                self.cache_data[key] = nod
            else:
                nod = node(key, item, None)
                self.back.next = nod
                self.back = nod
                self.cache_data[key] = nod
            self.count += 1

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key].value


my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
