"""
-------------------------------------------------------
[This function takes an integer greater than 0 as a parameter 
and returns a list of the factors that make up that number 
excepting the number itself. An integer's factors are the 
whole numbers that the integer can be evenly divided by.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""

from functions import list_factors

number = int(input("Enter number to determine factors of: "))

factors = list_factors(number)

print()
print(f"{factors}")
