"""
-------------------------------------------------------
[Searches through values for value and returns a list of
all indexes of its occurrence]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
from functions import many_search


values_input = input("Enter values: ")
value = input("Enter the value to search for: ")
values = [int(val.strip()) for val in values_input.split(',')]


indexes = many_search(values, int(value))

print()
print(f"{indexes}")
