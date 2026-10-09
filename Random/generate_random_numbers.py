'''
Write a Python program that generates and displays a random six-digit integer.

Your program should:

Generate a number from 100000 to 999999, inclusive.
Display the generated number.
Generate a different random number each time the program runs, when possible.
'''

import random
print(random.randint(100000, 999999))