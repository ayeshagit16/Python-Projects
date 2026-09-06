'''
TTL (Time-To-Live)
Discards based on the expiration time as per TTL
'''

import time
from collections import OrderedDict
from typing import Any

class TTLCache:
    '''Implement TTL Caching using OrderedDict and LRU'''

    def __init__(self, capacity: int, ttl: float):
        self.capacity = capacity
        self.ttl = ttl
        self._cache:OrderedDict[Any, tuple[Any, float]] = OrderedDict()


    def set(self, key, value):
        '''Insert or Update a Key-Value pair'''

        # if the key exists, remove it to reset its chronological position
        if key in self._cache:
            del self._cache[key]
        elif len(self._cache) >= self.capacity:
            self._cache.popitem(last=False)

        # store item with the current arrival timestamp
        self._cache[key] = (value, time.time())


    def get(self, key):
        '''Retrieve a value if it exists and has not expired'''

        if key not in self._cache:
            return None

        value, timestamp = self._cache[key]

        if time.time() - timestamp > self.ttl:
            del self._cache[key]
            return None

        self._cache.move_to_end(key)
        return value


    def delete(self, key):
        '''
        Manually removes item from the cache.
        Returns True if the item existed
        '''
        if key in self._cache:
            del self._cache[key]
            return True
        return False


    def clear_expired(self):
        '''Manually sweep and purge all expired keys across the cache'''

        now = time.time()
        # Create a static list of keys to avoid 'dictionary changed size during iteration' errors
        keys_to_check = list(self._cache.keys())

        for key in keys_to_check:
            # To verify existence in case a concurrent action changed it
            if key in self._cache:
                _, timestamp = self._cache[key]
                if now - timestamp > self.ttl:
                    del self._cache[key]


    def __len__(self):
        '''Returns the current number of items in the cache'''
        return len(self._cache)


cache = TTLCache(capacity=3, ttl=2.0)
cache.set("a","Apple")
cache.set("b","Banana")
cache.set("c","Cherry")
print(cache._cache)
cache.set("d", "Date")
print(cache._cache)
print(cache.get("a"))
print(cache.get("b"))
time.sleep(2.1)
print(cache.get("b"))
print(cache._cache)
cache.clear_expired()
print(cache._cache)
