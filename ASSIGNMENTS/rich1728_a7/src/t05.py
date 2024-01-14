"""
-------------------------------------------------------
[Determines whether a list is sorted.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""
from functions import verify_sorted

numbers = input("Enter list of numbers: ")

numbers_output = [int(x) for x in numbers.split(",")]

in_order, index = verify_sorted(numbers_output)

print()
print(f"{in_order}, {index}")
