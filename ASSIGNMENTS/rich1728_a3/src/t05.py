"""
-------------------------------------------------------
[Calculates distance an object has fallen due to gravity 
given the time it is fallen.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

from functions import falling_distance

falling_time = int(input("Enter time fallen (s): "))
distance = falling_distance(falling_time)

print()
print(f"The object has fallen {distance:.2f} meters in {falling_time} seconds.")
