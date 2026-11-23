'''
Problem: Write a Python program to print the following pattern for a given number of rows n=5:

        * 
      * * 
    *   * 
  *     * 
* * * * * 

'''
n = 7

for i in range(1, n + 1):
    leading_spaces = 2 * (n - i)
    inside_spaces = 2 * i - 3

    if i == 1:
        print(" " * leading_spaces + "*")
    elif i == n:
       print("* " * i)
    else:
      print(" " * leading_spaces + "*" + " " * inside_spaces + "*")
  