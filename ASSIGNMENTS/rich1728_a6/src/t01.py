"""
-------------------------------------------------------
[Asks the user to enter a series of strings representing 
game outcomes and counts how many times "purple" and "gold" 
appeared in the input.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""

from functions import total_wins

purple_count, gold_count = total_wins()
print()
print(f"({purple_count}, {gold_count})")
