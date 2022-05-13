#!/usr/bin/python3
"""
LIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Create a class LIFOCache that inherits
    from BaseCaching and is a caching system:
    """
    list = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None or item is None:
            return
        self.list.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.list[len(self.list) - 2]]
            print("DISCARD: {}".format(self.list[len(self.list) - 2]))

    def get(self, key):
        """
        Must return the value in self.cache_data linked
        to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
