"""
-------------------------------------------------------
[Calculates diameter of circle based off user input of the radius]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

from functions import diameter

r = float(input("Enter radius: "))
print()
d = diameter(r)
print(f"Diameter of circle: {d:.2f}")
