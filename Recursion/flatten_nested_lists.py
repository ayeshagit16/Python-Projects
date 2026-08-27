'''
Flatten a Deeply Nested List:
Base Case: if the list is empty, return an empty list
Recursive Case: if the first element is a list, flatten it + flatten the remainder.
                if it is an integer, extract it + flatten the remainder.
'''

def flatten_list(lst):
    '''Flatten a list into one single list'''

    if not lst:
        return []
    
    if isinstance(lst[0], list):
        return flatten_list(lst[0]) + flatten_list(lst[1:])
    else:
        return [lst[0]] + flatten_list(lst[1:])

print(flatten_list([1, [2, [3, 4]], 5]))
example = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten_list(example))
