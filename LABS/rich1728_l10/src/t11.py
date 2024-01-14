"""
-------------------------------------------------------
[Finds the last word with longest length in fh.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
from functions import find_longest

fh = open("words.txt", "r", encoding="utf-8")
longest_word = find_longest(fh)
print("file 'words.txt' open for reading")
print(f"'{longest_word}' is the last longest word")
