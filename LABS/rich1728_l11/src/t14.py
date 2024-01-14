"""
-------------------------------------------------------
[Transpose the contents of matrix. (Swap the rows and columns.)]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
from functions import matrix_transpose


user_input = input("Enter the matrix to transpose: ")

matrix = eval(user_input)

transposed = matrix_transpose(matrix)
print()
print(transposed)
