"""
-------------------------------------------------------
[Asks a user for a series of expenses in a month. Calculate the
total expenses and determines whether the user is in "Surplus",
"Deficit", or "Balanced" status.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

from functions import budget

available = float(input("Enter your budget: $"))
expenses, balance, status = budget(available)
print()
print(f"Total expenses: ${expenses:.2f}")
print(f"Remaining balance: ${balance:.2f}")
print(f"Budget status: {status}")
