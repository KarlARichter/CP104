"""
-------------------------------------------------------
[Determines the number of years to reach a target population.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

from functions import population_growth


target = int(input("Enter target population: "))
current = int(input("Enter current population: "))
rate = float(input("Enter population growth rate: "))


years = population_growth(target, current, rate)

print()
print(
    f"It will take {years} for the current population to reach the target population")
