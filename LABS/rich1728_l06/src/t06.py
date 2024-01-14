"""
-------------------------------------------------------
[Prints a triangle of height characters using the char 
character.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""
from functions import draw_triangle

height = int(input("Enter height: "))
char = str(input("Enter char: "))

draw_triangle(height, char)
