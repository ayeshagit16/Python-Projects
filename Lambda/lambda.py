'''
Can you use if without else?
No. A lambda function must always return a value. 
If the if condition evaluates to False, Python needs to know what to return, making the else clause syntactically mandatory.
'''

lamb_func = lambda x, y: x - y if x > y else x + y

print(lamb_func(5, 4))

print(lamb_func(2, 4))