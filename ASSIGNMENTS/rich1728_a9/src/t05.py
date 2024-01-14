"""
-------------------------------------------------------
[Get information from a file of file_handle and grades.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""

from functions import student_stats


file_handle = open("students.txt", "r", encoding="utf-8")

l_id, h_id, avg = student_stats(file_handle)


print(f"{l_id}, {h_id}, {avg}")
