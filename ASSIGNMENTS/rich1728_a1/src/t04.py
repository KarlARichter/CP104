"""
------------------------------------------------------------------------
[The user inputs the cost of 1 dosa and the amount, the program then gives 
the user the total cost]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-09-11"
------------------------------------------------------------------------
"""


dosa = float(input("Cost of 1 dosa: "))
numDosa = float(input("Number of dosa: "))
print("Total cost of", numDosa, "dosas: $", dosa * numDosa)
