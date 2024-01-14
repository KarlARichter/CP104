"""
-------------------------------------------------------
[Calculates future population given various factors]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

from functions import population

current_population = int(input("Enter current population: "))
average_births = int(input("Enter average seconds between births: "))
average_deaths = int(input("Enter average seconds between deaths: "))
average_immigrants = int(input("Enter average seconds between immigrations: "))
years_calculate = int(input("Enter years to calculate new population: "))

new_population = population(current_population, average_births,
                            average_deaths, average_immigrants, years_calculate)

print(
    f"\nProjected population after {years_calculate} years: {new_population}")
