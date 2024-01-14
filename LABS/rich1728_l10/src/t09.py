"""
-------------------------------------------------------
[Counts the number of appearances of value in fh.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""

from functions import count_frequency_value

fh = open("numbers.txt", "r", encoding="utf-8")

value = int(input("Value to count: "))
count = count_frequency_value(fh, value)

print()
print("file 'numbers.txt' open for reading")
print(f"Value to count: {value}")
print(f"{value} appears {count} time(s)")
