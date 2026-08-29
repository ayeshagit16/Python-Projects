'''
LRU (Least Recently Used)
LRU discards the least recently used items first when the cache is full.
Using collcetions.OrderedDict
'''

from collections import OrderedDict

class LRUCache:
    '''Implement LRU Caching'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        # 1. if the key is not found
        if key not in self.cache:
            return -1

        # 2. if the key is found
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):

        # Key is found, move it to end
        if key in self.cache:
            self.cache.move_to_end(key)

        # key found or not found, update or add accordingly
        self.cache[key] = value

        # check cache capacity irrespective and remove the least recently used item (the first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def clear(self):
        self.cache.clear()

cache = LRUCache(2)
cache.put(1, "A")
print(cache.cache)
print(cache.get(2))
cache.put(2, "B")
print(cache.cache)
cache.put(3, "C")
print(cache.cache)
cache.clear()
print(cache.cache)
