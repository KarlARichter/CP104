"""
-------------------------------------------------------
[This program prompts the user to enter the number of flyers 
and the number of volunteers, and prints the number of flyers 
per volunteer and the number of flyers left over.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""

numFLY = int(input("Number of flyers: "))
numVOL = int(input("Number of volunteers: "))

flyer_VOL = numFLY // numVOL
flyer_EXTRA = numFLY % numVOL


print("\nFlyers per volunteer:", flyer_VOL)
print("Flyers left over:", flyer_EXTRA)
