"""
-------------------------------------------------------
[Calculates a prints a table of how much a worker earns
between age and retirement at 65]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
from functions import retirement

age = int(input("Enter your current age: "))
salary = float(input("Enter your initial salary: $"))
increase = float(input("Enter annual salary increase percentage (%): "))

retirement(age, salary, increase)
