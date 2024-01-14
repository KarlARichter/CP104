"""
-------------------------------------------------------
[Converts total seconds into days, hours, minutes, and seconds]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

from functions import time_split

TOTAL_SECONDS = int(input("Enter total seconds: "))

DAYS, HOURS, MINUTES, SECONDS = time_split(TOTAL_SECONDS)

print(f"\n{DAYS} days, {HOURS} hours, {MINUTES} minutes, and {SECONDS} seconds")
