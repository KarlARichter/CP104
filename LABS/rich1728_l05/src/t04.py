"""
-------------------------------------------------------
[Determines closest value of two values to a target value]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
from functions import closest

target = float(input("Enter target number: "))
v1 = float(input("Enter first number: "))
v2 = float(input("Enter second number: "))

result = closest(target, v1, v2)

print()
print(f"{result} is the closer number to {target}")
