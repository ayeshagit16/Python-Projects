'''
String Reversal:
Base Case: if string is empty or has a single character return it
Recursive Case: last character + reverse of the remaining string
'''

def str_reverse(s):
    '''Reverese the elements of a string'''
    if s == "":
        return ""
    # elif len(s) == 1:
        # return s
    else:
        return s[-1] + str_reverse(s[:-1])

print(str_reverse("hello world"))
print(str_reverse(""))
print(str_reverse("K"))