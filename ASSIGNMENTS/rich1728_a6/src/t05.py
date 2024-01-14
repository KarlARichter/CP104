"""
-------------------------------------------------------
[Determines the sum of factors of an integer not including
the integer itself]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""

from functions import factor_summation

number = int(input("Enter number greater than 1: "))

total = factor_summation(number)

print()
print(f"The sum of factors of the integer {number} is {total}")
