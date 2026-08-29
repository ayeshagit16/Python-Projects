'''
FIFO (First-In-First-Out)
FIFO operates on the principle that the first item added to the cache is the first one to be removed when the cache is full.
Caching scenario where all items have equal importance.
Using collcetions.OrderedDict
'''

from collections import OrderedDict 

class FIFOCache:
    '''Implement FIFO Caching'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        return self.cache.get(key, -1)

    def put(self, key, value):

        # OnlyIf the key is not already in the cache and the cache is full
        if key not in self.cache and len(self.cache) >= self.capacity:
            # Remove the first item in the cache (FIFO eviction)
            self.cache.popitem(last=False)
    
        # insert or update as per requirement
        self.cache[key] = value

cache = FIFOCache(3)
cache.put(1, "A")
print(cache.get(1))
print(cache.get(2))
cache.put(2, "B")
cache.put(3, "C")
print(cache.cache)
cache.put(4, "D")
print(cache.capacity)
print(cache.cache)
print(cache.get(1))
