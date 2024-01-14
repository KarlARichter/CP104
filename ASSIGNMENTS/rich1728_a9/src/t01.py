"""
-------------------------------------------------------
[Prints first count lines of file_handle. Line numbering 
starts at 0. If length of file is shorter than count, 
stops printing after last line of file.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
from functions import file_top

file_handle = open("students.txt", "r", encoding="utf-8")

count = int(input("Enter amount of lines to count: "))
print()
file_top(file_handle, count)
file_handle.close()
