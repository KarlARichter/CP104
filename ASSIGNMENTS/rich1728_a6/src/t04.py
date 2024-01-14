"""
-------------------------------------------------------
[Counts the number of digits in an integer.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""


from functions import count_of_digits

number = int(input("Enter an int: "))

digits = count_of_digits(number)
print()
print(f"Number of digits in the int {number} is {digits}")
