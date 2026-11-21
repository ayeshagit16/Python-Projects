'''
Problem: Write a Python program to print the following pattern for a given number of rows n=5:


    * 
   * * 
  * * * 
 * * * * 
* * * * * 

Inverted Centered Pyramid:

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

n= 5
loop = n-1

for i in range(1, n+1):
    print(" " * loop + "* " * i)
    loop -= 1

loop = 0
for i in range(n, 0, -1):
    print(" " * loop + "* " * i)
    loop += 1