'''Syntax:  result = reduce(lambda acc, val: expression, iterable)'''

from functools import reduce

numbers = [23, 89, 12, 45, 67]

# Finding the Maximum Value
res = reduce(lambda acc, val:acc if acc > val else val, numbers)
print(res)


numbers = [1, 2, 3, 4]
product = reduce(lambda acc, val: acc * val, numbers)
print(product)

# with initial value
new_prod = reduce(lambda x, y: x*y, numbers, 10)
print(new_prod)
