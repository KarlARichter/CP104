"""
-------------------------------------------------------
[Determines if number is a prime number.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""

from functions import detect_prime

number = int(input("Enter number: "))

prime = detect_prime(number)

print()
print(f"{prime}")
