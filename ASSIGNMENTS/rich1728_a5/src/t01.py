"""
-------------------------------------------------------
[Calculates and returns the factorial of number.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
from functions import calc_factorial

number = int(input("Enter number to calculate factorial of: "))

product = calc_factorial(number)

print()
print(f"{number}! = {product}")
