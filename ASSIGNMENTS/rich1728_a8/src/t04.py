"""
------------------------------------------------------------------------
[Determines if an ISBN string is valid. An ISBN string is valid]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-11-12"
------------------------------------------------------------------------
"""

from functions import valid_isbn
isbn = str(input("Enter ISBN: "))
is_valid = valid_isbn(isbn)

print()
print(f"{is_valid}")
