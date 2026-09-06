'''
MRU (Most Recently Used)
MRU discards the most recently used items first.
'''

from collections import OrderedDict

class MRUCache:
    '''Implement MRU Caching'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem()
        self.cache[key] = value

cache = MRUCache(2)
cache.put("A", 1)
cache.put("B", 2)   # A, B
print(cache.cache)
cache.get("A")      # B, A
print(cache.cache)
cache.put("C", 3)
print(cache.cache)
