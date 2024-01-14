"""
-------------------------------------------------------
[Converts square footage to acres]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

from functions import footage_to_acres

square_feet = float(input("Enter amount of acres: "))
acres = footage_to_acres(square_feet)

print()
print(f"{square_feet} square feet -> {acres} acres")
