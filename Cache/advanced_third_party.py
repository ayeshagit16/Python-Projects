'''Advanced/Third-party Caching(Time-To-Live/TTL)'''

# pip install cachetools

from cachetools import TTLCache, cached

my_ttl_cache = TTLCache(maxsize=120, ttl=300)  # max size of 120 items and items expire after 300 seconds

@cached(my_ttl_cache)
def get_api_response(url):
    '''Get API response'''
    return f"Response from {url}"

print(my_ttl_cache)
print(get_api_response("http://google.com/"))
print(get_api_response("https://www.wikipedia.org/"))
print(my_ttl_cache)
print("ttl:", my_ttl_cache.ttl)
print("keys:", my_ttl_cache.keys())
print("Items:", my_ttl_cache.items())
my_ttl_cache.clear()
print(my_ttl_cache)
