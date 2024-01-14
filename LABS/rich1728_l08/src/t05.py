"""
-------------------------------------------------------
[Generates a sorted list of unique lottery numbers]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""

from functions import get_lotto_numbers

n = int(input("Enter the number of lottery numbers to generate: "))
low = int(input("Enter the low value of the lottery number range: "))
high = int(input("Enter the high value of the lottery number range: "))

numbers = get_lotto_numbers(n, low, high)

print()
print(f"{numbers}")
