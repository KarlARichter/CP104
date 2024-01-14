"""
-------------------------------------------------------
[Calculates future population given various factors]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

from functions import time_values

TOTAL_SECONDS = int(input("Enter total seconds: "))

DAYS, HOURS, MINUTES = time_values(TOTAL_SECONDS)

print(f"\n{DAYS} days, {HOURS} hours, and {MINUTES} minutes")
