"""
-------------------------------------------------------
[Parses a given product code and prints whether the various parts are valid.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""

from functions import validate_code

product_code = str(input("Enter product code: "))

category, digits, qualifiers = validate_code(product_code)

print()
print(f"{category}, {digits}, {qualifiers}")
