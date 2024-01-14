"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""
from functions import colour_combine

rgb_colour1 = str(input("Enter first colour: "))
rgb_colour2 = str(input("Enter second colour: "))

rgb_colour = colour_combine(rgb_colour1, rgb_colour2)

print()
print(f"{rgb_colour1} mixed with {rgb_colour2} gives {rgb_colour}")
