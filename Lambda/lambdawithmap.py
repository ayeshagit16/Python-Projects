'''
Applies the given function to every item in one or more iterable and returns an iterator object containing transformed results.
'''

list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(map(lambda x, y: x * y, list1, list2)))

numbers = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, numbers)))
#vs
print([x**2 for x in numbers])
