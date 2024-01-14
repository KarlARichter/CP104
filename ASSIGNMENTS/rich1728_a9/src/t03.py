"""
-------------------------------------------------------
[Evaluates the contents of a file by counting upper-case letters,
lower-case letters, digits, white-spaces (including end-of-line
characters), and remaining characters.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""

from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")

ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)

print(f"{ucount}, {lcount}, {dcount}, {wcount}, {rcount}")


file_handle.close()
