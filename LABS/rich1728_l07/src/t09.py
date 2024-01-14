"""
-------------------------------------------------------
[Asks a user for an integer value between low and high, and
continues asking until an acceptable value is input]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""

from functions import get_int

low = int(input("Enter lowest number: "))
high = int(input("Enter highest number: "))

value = get_int(low, high)

print()
print(f"{value}")
