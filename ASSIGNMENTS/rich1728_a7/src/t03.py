"""
-------------------------------------------------------
[Finds the indexes of target_number in numbers.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""

from functions import get_indexes

numbers = input("Enter numbers: ")
target_number = input("Enter number to search for: ")
numbers_split = [int(val.strip()) for val in numbers.split(',')]

index_list = get_indexes(numbers_split, int(target_number))

print()
print(f"{index_list}")
