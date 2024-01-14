"""
-------------------------------------------------------
[Calculates and returns fraction values.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""

from functions import multiply_fractions

num1 = int(input("Enter first numerator: "))
den1 = int(input("Enter second numerator: "))
num2 = int(input("Enter first denominator: "))
den2 = int(input("Enter second denominator: "))

num, den, product = multiply_fractions(num1, den1, num2, den2)

print()
print(f"{num}, {den}, {product}")
