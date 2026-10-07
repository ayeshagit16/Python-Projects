'''
Can you use if without else?
No. A lambda function must always return a value. 
If the if condition evaluates to False, Python needs to know what to return, making the else clause syntactically mandatory.
'''

lamb_func = lambda x, y: x - y if x > y else x + y

print(lamb_func(5, 4))

print(lamb_func(2, 4))

make_pairs = lambda list1, list2: [(x, y) for x in list1 for y in list2]
print(make_pairs(['a', 'b'], [1, 2]))

double_evens = lambda numbers:[x*2 for x in numbers if x%2 == 0]
print(double_evens([1, 2, 3, 4]))
