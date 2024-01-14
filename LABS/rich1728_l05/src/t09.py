"""
-------------------------------------------------------
[Takes wind speed and places it under category based 
on the speed]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
from functions import wind_speed

speed = int(input("Enter speed of winds: "))
category = wind_speed(speed)

print()
print(f"{speed} km/h falls under the following category: {category}")
