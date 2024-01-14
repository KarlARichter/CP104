"""
-------------------------------------------------------
[Determines how long it takes to mow a rectangular lawn]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

from functions import lawn_mow_time

width = float(input("Enter width of lawn: "))
length = float(input("Enter length of lawn: "))
speed = float(input("Enter speed of mowing: "))

time = lawn_mow_time(width, length, speed)

print()
print(f"It will take {time} minutes to mow the lawn")
