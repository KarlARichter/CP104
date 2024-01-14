"""
-------------------------------------------------------
[Adds line numbers to a file. Contents of fh_write contain contents
of fh_read where every line has line numbers added to the beginning
of the line in the format [number]. Line numbering starts at 0.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""

from functions import line_numbering

fh_read = open("wilde.txt", "r", encoding="utf-8")
fh_write = open("wilde_numbered.txt", "w", encoding="utf-8")

line_numbering(fh_read, fh_write)
