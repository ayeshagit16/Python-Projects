'''
Problem: Write a Python program to print the following pattern for a given number of rows n=5:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

Inverted Left-Angled Triangle:
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

'''

n = 5
loop = n - 1
for i in range(1, n + 1):
    print(" " * (2 * loop) + "* " * i)
    loop -= 1

rev_loop = 0
for i in range(n, 0, -1):
    print(" " * (2 * rev_loop) + "* " * i)
    rev_loop += 1
