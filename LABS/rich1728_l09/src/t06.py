"""
-------------------------------------------------------
[Checks whether the given string is palindrome or not. A palindrome is
a string the reads the same forwards as backwards. Case is ignored.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""

from functions import is_palindrome

s = str(input("Enter word to check if it is a palindrome: "))

palindrome = is_palindrome(s)

print()
print(f"{palindrome}")
