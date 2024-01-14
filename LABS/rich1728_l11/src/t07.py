"""
-------------------------------------------------------
[Determines the first locations [row, column] of smallest 
and largest values in a 2D list]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-12"
-------------------------------------------------------
"""

from functions import find_position


user_input = input("Enter the matrix: ")

matrix = eval(user_input)

min_loc, max_loc = find_position(matrix)

print()
print(f"{min_loc}, {max_loc}")
