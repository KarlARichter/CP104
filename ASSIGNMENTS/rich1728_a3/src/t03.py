"""
-------------------------------------------------------
[Extracts the year, month, and day from a date number in the format YYYYMMDD]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""

from functions import extract_date

date_number = int(input("Enter date: "))
year, month, day = extract_date(date_number)

print(f"Extracted date: {year}, {month}, {day}")
