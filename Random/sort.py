"""Question:

How can you rearrange this list so that all even numbers come before the
odd numbers?

Complete the TODOs without changing the original list.
"""

numbers = [4, 5, 6, 7, 2, 3, 11, 13]

# TODO: Create a list with the even numbers first and the odd numbers after.
# TODO: Print the resulting list.

even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

res = even_nums + odd_nums
print(res)

print(sorted(even_nums) + sorted(odd_nums))