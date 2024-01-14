"""
-------------------------------------------------------
[Returns the name of a month given its number]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""

from functions import get_month_name

m = int(input("Enter number of month: "))

name = get_month_name(m)

print()
print(f"{name}")
