'''A custom generator in Python is a special type of function that returns an iterable object. 
   It allows you to produce a sequence of values over time using the yield keyword instead of return. 
   This makes it highly memory-efficient because it creates values on demand (lazy evaluation) rather than 
        storing them in memory all at once
'''

def fibonacci_gen(n):
    """A custom generator that yields the first n Fibonacci numbers."""

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


fibo_gen = fibonacci_gen(10)

for num in fibo_gen:
    print(num)

print(list(fibonacci_gen(5)))

fib_gen = fibonacci_gen(3)
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
# print(next(fib_gen))   raises error StopIteration
