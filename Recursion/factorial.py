'''
Factorial of a number:
Base Case: if n <=1, return 1
Recursive Case: n * fact(n-1)
'''


def fact(n):
    '''Find the factorial of a number'''

    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # Output: 120
print(fact(2))  # Output: 2