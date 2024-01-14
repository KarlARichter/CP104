"""
-------------------------------------------------------
[Appends a number to the end of fh. The number appended
is the maximum of all the numbers currently in the file.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
from functions import append_max_num


fh = open("numbers.txt", "r+", encoding="utf-8")

num = append_max_num(fh)

print("file 'numbers.txt' open for reading and writing")
print(f"{num} is appended")
