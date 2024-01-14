"""
------------------------------------------------------------------------
[Asks a user to enter n values, then calculates and returns
the minimum, maximum, total, and average of those values.]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-10-02"
------------------------------------------------------------------------
"""

from functions import statistics

n = int(input("Enter amount of statistics: "))

minimum, maximum, total, average = statistics(n)

print()
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
