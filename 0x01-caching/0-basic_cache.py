#!/usr/bin/python3
"""
Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system:
    """
    def put(self, key, item):
        """Must assign to the dictionary self.cache_data the item value for
        the key key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
