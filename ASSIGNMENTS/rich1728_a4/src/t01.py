"""
-------------------------------------------------------
[Returns the name of a day of the week given an integer 
day number. Day 1 is Sunday, day 7 is Saturday]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""
from functions import day_name

day_num = int(input("Enter number for day: "))
day = day_name(day_num)

print()
print(f"The number {day_num} corresponds to {day}")
