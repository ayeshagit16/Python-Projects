'''
Write a Python program that asks the user to enter a sentence and prints the sentence with all punctuation marks removed.

For example:

Input: Hello, world! How are you?
Output: Hello world How are you
Your program should remove punctuation without changing the order of the remaining characters. Preserve spaces and letters.
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''
import re
import string
import unicodedata

sentence = input("Enter a sentence: ")

# 1.
result = " ".join(re.findall(r"\w+", sentence))
print(result)

# 2.
result = "".join((char for char in sentence if char not in string.punctuation))
result = " ".join(result.split())
print(result)


# 3.
clean_text = "".join(char for char in sentence if not unicodedata.category(char).startswith("P"))
clean_text = " ".join(clean_text.split())
print(clean_text)

# use senetence:well-known, isn’t it?  Yes!     -- to see the difference in all 3