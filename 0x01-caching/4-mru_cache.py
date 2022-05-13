#!/usr/bin/python3
""" 3-main LRU Cache """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Create a class MRUCache that inherits from BaseCaching
    and is a caching system:
    """
    list = []
    dict = {}

    def __init__(self):
        """ Init instance BaseCaching """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the
        item value for the key key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            """ find key by value """
            for k, v in self.dict.items():
                if v == 1:
                    to_remove = k
                    del self.cache_data[to_remove]
                    break

            self.dict = self.cache_data.copy()
            self.list = list(self.dict.keys())
            for i in self.list:
                self.dict[i] = 0
            self.dict[key] += 1
            print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.dict = self.cache_data.copy()
        self.list = list(self.dict.keys())
        for i in self.list:
            self.dict[i] = 0
        self.dict[key] += 1
        return self.cache_data[key]
