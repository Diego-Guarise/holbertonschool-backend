#!/usr/bin/python3
"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Use self.cache_data - dictionary from
    the parent class BaseCaching """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ 
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            list_aux = list(self.cache_data.keys())
            del self.cache_data[list_aux[0]]
            self.cache_data[key] = item
            print("DISCARD: {}".format(list_aux[0]))

    def get(self, key):
        """
        Must return the value in self.cache_data linked
        to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]