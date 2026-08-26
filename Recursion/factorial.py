'''Factorial of a number'''
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # Output: 120
print(fact(2))  # Output: 2