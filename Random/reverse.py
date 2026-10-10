'''
Write a Python program that asks the user to enter an integer and prints the integer with its digits reversed.

For example:

Input: 12345 → Output: 54321
Input: 700 → Output: 7
Input: -246 → Output: -642
Your program should preserve the sign of negative numbers. Do not convert the integer to a string to reverse it.
'''

def reverse_number():
    num = int(input("Enter your number: "))

    rem = 0
    sign = -1 if num < 0 else 1
    num = abs(num)

    while num > 0:
        rem = (rem * 10) + (num % 10)
        num = num // 10

    return rem * sign

result = reverse_number()
print(result)
