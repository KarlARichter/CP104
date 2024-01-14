"""
------------------------------------------------------------------------
[Calculates sums of elements of two lists. Lists must be the same length]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-11-09"
------------------------------------------------------------------------
"""

from functions import list_sums

source1 = input("Enter first list separated by commas: ").split(",")
source2 = input("Enter second list separated by commas: ").split(",")

target = list_sums(source1, source2)

print()
print(f"{target}")
