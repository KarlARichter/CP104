"""
-------------------------------------------------------
[Copies n record from fh_1 (starting from the beginning of the file) to fh2]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
from functions import file_copy_n

n = int(input("Number of lines to copy: "))
fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w", encoding="utf-8")

file_copy_n(fh_1, fh_2, n)

print()
print("Copying 'words.txt' to 'new_words.txt'")
print(f"Number of lines to copy: {n}")
