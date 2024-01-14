"""
-------------------------------------------------------
[Alters the contents of minuend so that it does not contain
any values in subtrahend]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""

from functions import list_subtract

minuend_input = input("Enter the minuend list: ")
subtrahend_input = input("Enter the subtrahend list: ")

minuend = [int(x) for x in minuend_input.split(",")]
subtrahend = [int(x) for x in subtrahend_input.split(",")]

list_subtract(minuend, subtrahend)

print()
print(f"minuend after: {minuend}")
