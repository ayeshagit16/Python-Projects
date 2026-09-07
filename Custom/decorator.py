'''Writing custom decorators and using functools.wraps to save the original functions metadata'''

import time
from functools import wraps

def time_it(prefix="[LOG]"):
    '''A decorator that measures the execution time of a function'''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()

            execution_time = end_time - start_time
            print(f"{prefix} '{func.__name__}' took {execution_time:.6f} seconds to execute")
            return result
        return wrapper
    return decorator


@time_it(prefix="[PERF]")
def compute_squares(n):
    return [i ** 2 for i in range(n)]


squares = compute_squares(100_000)  # same as 100000, In Python, the underscore in a number is just a visual separator for readability.
squares = compute_squares(1_000_000)
