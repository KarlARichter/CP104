"""
-------------------------------------------------------
[Returns statistics on a 2D list.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
from functions import matrix_stats

user_input = input("Enter the matrix: ")

matrix = eval(user_input)

smallest, largest, total, average = matrix_stats(matrix)
print(f"{smallest}, {largest}, {total}, {average}")
