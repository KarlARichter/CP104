"""
-------------------------------------------------------
[Uses a for loop to sum values from start by increment.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-09"
-------------------------------------------------------
"""
from functions import range_addition

start = int(input("Enter start value: "))
increment = int(input("Enter increment value: "))
count = int(input("Enter count value: "))


total = range_addition(start, increment, count)

print()
print(f"{total}")
