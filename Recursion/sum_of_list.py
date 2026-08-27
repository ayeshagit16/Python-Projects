'''
Sum of elements in a list:
Base Case: if list is empty, return 0
Recursive Case: first element + sum of remaining list
'''

def sum_of_list(lst):
    '''Calculate the sum of all the elements in the list'''

    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])

print(sum_of_list([1, 3, 4, 2]))
print(sum_of_list([1, -3, 4, 5]))