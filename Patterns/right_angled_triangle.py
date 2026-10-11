'''
Problem: Write a Python program to print the following pattern for a given number of rows n=5:
* 
* * 
* * * 
* * * * 
* * * * * 

Inverted Right-Angled Triangle:
* * * * * 
* * * * 
* * * 
* * 
* 

'''

n = 5
for i in range(1, n+1):
    print('* ' * i)


for i in range(n, 0, -1):
    print('* ' * i)
