
#!/usr/bin/python3
""" 2-main LIFO """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherit from BaseCaching """
    list_aux = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add LIFO """
        if key is None or item is None:
            return
        self.list_aux.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.list_aux[len(self.list_aux) - 2]]
            print("DISCARD: {}".format(self.list_aux[len(self.list_aux) - 2]))

    def get(self, key):
        """ Get FIFO """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]