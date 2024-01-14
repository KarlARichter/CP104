"""
------------------------------------------------------------------------
[Create a new sentence with added space between words. Words start with 
upper-case characters]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-10-21"
------------------------------------------------------------------------
"""

from functions import add_spaces

sentence = str(input("Enter sentence here: "))

spaced = add_spaces(sentence)

print()
print(f"{spaced}")