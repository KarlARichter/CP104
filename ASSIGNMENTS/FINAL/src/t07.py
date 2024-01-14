"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
from t07_functions import line_lengths


n = int(input("Enter number of lines to copy: "))
f_in = open("source.txt", "r", encoding="utf-8")
f_short = open("short.txt", "w+", encoding="utf-8")
f_long = open("long.txt", "w+", encoding="utf-8")

short_lines, long_lines = line_lengths(f_in, f_short, f_long, n)

print(f"Short lines: {short_lines}")
print(f"Long lines: {long_lines}")
