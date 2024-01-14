"""
-------------------------------------------------------
[Sums and returns the total of all odd numbers from 1 to 
num (inclusive).]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""

from functions import sum_odd

num = int(input("Enter number: "))
total = sum_odd(num)

print()
print(f"The total of all odd numbers from 1 to {num} is {total}")
