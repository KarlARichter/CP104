"""
-------------------------------------------------------
[Describes a mass in terms of its weight.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
from functions import get_weight

mass = float(input("Enter weight of object: "))

weight, message = get_weight(mass)

print()
print(f"Object is {message} weight")
