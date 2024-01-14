"""
-------------------------------------------------------
[Asks a user to enter a series of positive numbers, then calculates
and returns the minimum, maximum, total, and average of those numbers.
Stop processing values when the user enters a negative number.
The first number entered must be positive]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""

from functions import positive_statistics

minimum, maximum, total, average = positive_statistics()
print(
    f"(Minimum: {minimum:.2f}, Maximum: {maximum:.2f}, Total: {total:.2f}, Average: {average:.2f})")
