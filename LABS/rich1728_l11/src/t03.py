"""
-------------------------------------------------------
[Prints the contents of a 2D list in a formatted table.
Prints float values with 2 decimal points and prints row and
column headings]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from functions import print_matrix_num

matrix = int(input("Enter matrix: "))
value_type = str(input("Enter value type: "))

print_matrix_num(matrix, 'float')
print_matrix_num(matrix, 'int')
