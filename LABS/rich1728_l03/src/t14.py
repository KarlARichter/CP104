"""
-------------------------------------------------------
[This program asks the user to enter a number of minutes 
as int and calculates the number of days, hours, and 
minutes and prints them to the screen.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

MIN = int(input("Enter number of minutes: "))

DAYS = MIN // (24 * 60)
HOURS = (MIN % (24 * 60)) // 60
REMAIN = MIN % 60

print(f"There are {DAYS} days, {HOURS} hours, and {REMAIN} minutes in {MIN} minutes")
