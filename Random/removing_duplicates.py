'''
Write a Python program that takes a list of numbers as input and removes duplicate values while preserving the original order of the first occurrence of each element. For example, if the input is:
[4, 2, 4, 3, 2, 5, 3]

the output should be:
[4, 2, 3, 5]

Your program should:

accept a list as input
keep only the first occurrence of each value
print the resulting list
work for any list of values, not just numbers
Do not use built-in set operations to solve it.
'''

from collections import Counter


numbers = [4, 2, 4, 3, 2, 5, 3]

# 1.
res_dict = Counter(numbers)
new_list = res_dict.keys()
print(list(new_list))

# 2. Brute Force
res = {}
for item in numbers:
    if item in res.keys():
        res[item] += 1
    else:
        res[item] = 1

print(list(res.keys()))

# 3. Simplest brute force
result = []

for item in numbers:
    if item not in result:
        result.append(item)
print(result)
