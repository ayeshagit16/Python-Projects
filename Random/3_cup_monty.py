'''
Write a Python program to simulate the 3-cup Monty Hall problem.

Requirements:

Randomly place the prize behind one of 3 cups.
Let the user choose a cup.
Reveal one of the other cups that does not contain the prize.
Ask the user whether they want to stay with their original choice or switch.
Print whether the user won or lost.
Run multiple rounds and compare the win rates for “stay” vs “switch”.
'''

import random

cup = ['0', 'X', 'O']
random.shuffle(cup)

print(cup)

choice = int(input("Enter your cup position 0, 1, 2: "))
option = input("Are you sure you want to keep the original choice or switch: ")
if option.upper() == "YES":
    choice = int(input("Enter your cup position 0, 1, 2: "))

if cup[choice].upper() == 'X':
    pass