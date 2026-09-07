'''
Fibonacci Series:
Base Case: if n=0 return 0, if n=1 return 1
Recursive Case: fibonacci(n-1) + fibonacci(n-2)
'''
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_series(n):
    '''Find the nth number in the fibonacci series'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)


def generate_fibonacci(count, index=0):
    '''Generate count Fibonacci numbers recursively.'''
    if index == count:
        return []
    return [fibonacci_series(index)] + generate_fibonacci(count, index + 1)

print(fibonacci_series(7))
numbers = generate_fibonacci(1)
print(numbers)
