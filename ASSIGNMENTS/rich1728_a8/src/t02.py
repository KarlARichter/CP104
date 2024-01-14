"""
------------------------------------------------------------------------
[Pluralizes a string according to the rules]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-10-20"
------------------------------------------------------------------------
"""

from functions import pluralize


string = str(input("Enter word: "))

pluralized = pluralize(string)

print()
print(f"{pluralized}")