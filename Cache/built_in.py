'''
Built-in Caching Decorators:
Eviction Policy :-
@functools.cache: None (Unbounded)
@functools.lru_cache:Least Recently Used
'''

import time
from functools import cache, lru_cache

@cache
def user_data(user_id):
    '''Fetch user data'''
    time.sleep(2)
    return f" User data for {user_id}"


@lru_cache(maxsize=128)
def calculate_power(base, exponent):
    '''Calculate power of a number/base'''
    return base ** exponent

print(calculate_power.cache_info())
print(calculate_power(2, 3))
print(calculate_power.cache_info())
print(calculate_power(2, 3))
print(calculate_power.cache_info())
calculate_power.cache_clear()
print(calculate_power.cache_info())
