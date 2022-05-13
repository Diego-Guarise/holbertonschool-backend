#!/usr/bin/python3
""" 3-main LRU Cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Create a class LRUCache that inherits from
    BaseCaching and is a caching system:
    """
    list = []

    def __init__(self):
        """ Init instance BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value for the key key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if self.list.count(key) == 0:
            self.list.append(key)
        else:
            for i in self.list:
                if i == key:
                    self.list.remove(i)
                    break
            self.list.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.list[0]]
            to_remove = self.list[0]
            self.list.remove(self.list[0])
            print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """
        Must return the value in self.cache_data linked
        to key.
        """
        if key is None or key not in self.cache_data:
            return None
        if self.list.count(key) == 0:
            self.list.append(key)
        else:
            for i in self.list:
                if i == key:
                    self.list.remove(i)
                    break
            self.list.append(key)
        return self.cache_data[key]
