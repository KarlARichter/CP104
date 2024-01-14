"""
-------------------------------------------------------
[Returns data about the categories of values in a list]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
from functions import list_categorize

user_input = input("Enter numbers: ")

values = [int(value) for value in user_input.split(',')]
negatives, positives, zeroes, evens, odds = list_categorize(values)

print()
print(f"The number of negatives: {negatives}")
print(f"The number of positives: {positives}")
print(f"The number of zeroes: {zeroes}")
print(f"The number of evens: {evens}")
print(f"The number of odds: {odds}")
