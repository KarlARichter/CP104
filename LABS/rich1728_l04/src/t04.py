"""
-------------------------------------------------------
[Calculates and returns the slant height, area, and
volume of a square pyramid given the base and perpendicular height.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
from functions import square_pyramid

b = float(input("Enter the base: "))
h = float(input("Enter the height: "))

sh, area, vol = square_pyramid(b, h)

print(sh, ",", area, ",", vol)
