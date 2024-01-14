"""
-------------------------------------------------------
[Returns sentence depending on number inputed by user]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""
from functions import hoo_rah

number = int(input("Enter number: "))
sentence = hoo_rah(number)

print()
print(f"Your sentence is: {sentence}")
