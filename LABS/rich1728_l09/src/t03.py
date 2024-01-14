"""
-------------------------------------------------------
[Parses a given product code]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""

from functions import parse_code

product_code = str(input("Enter product code: "))

pc, pi, pq = parse_code(product_code)

print()
print(f"{pc}, {pi}, {pq}")
