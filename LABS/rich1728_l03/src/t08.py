"""
-------------------------------------------------------
[Prints the resulting total cubic metres with amounts lined up]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-24"
-------------------------------------------------------
"""

DIRT = float(input("Enter amout of dirt (m^3):"))
GRAVEL = float(input("Enter amout of gravel (m^3):"))
SAND = float(input("Enter amout of sand (m^3):"))
TOTAL = DIRT + GRAVEL + SAND

print()
print("Material   Cubic Metres")
print(f"Dirt     {DIRT:5.1f}")
print(f"Gravel   {GRAVEL:5.1f}")
print(f"Sand     {SAND:5.1f}")
print(f"Total    {TOTAL:5.1f}")
