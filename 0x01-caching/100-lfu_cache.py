#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching
and is a caching system:
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    Create a class LFUCache that inherits from BaseCaching
    and is a caching system:
    """
    def __init__(self):
        """
        Init instance BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """
        Reorders the items in this cache
        """
        list = []
        freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(list) == 0:
                list.append(i)
            elif key_freq[1] < self.keys_freq[list[-1]][1]:
                list.append(i)
        list.reverse()
        for pos in list:
            if self.keys_freq[pos][1] >= freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, freq])

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
