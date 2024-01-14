"""
-------------------------------------------------------
[Extracts positive integers from a file into a list of integers.
Numbers are comma-delimited. Non-numeric tokens are ignored.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""

from functions import read_integers

file_handle = open("numbers.txt", "r", encoding="utf-8")

number_list = read_integers(file_handle)

print(number_list)

file_handle.close()
