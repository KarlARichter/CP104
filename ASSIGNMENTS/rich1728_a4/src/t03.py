"""
-------------------------------------------------------
[ Returns the average of the two largest values of 
val1, val2, and val3.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
from functions import largest_average

val1 = float(input("Enter first number: "))
val2 = float(input("Enter second number: "))
val3 = float(input("Enter third number: "))

average = largest_average(val1, val2, val3)

print()
print(f"The average of the two largest numbers is {average}")
