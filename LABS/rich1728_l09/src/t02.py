"""
-------------------------------------------------------
[Returns whether a url represents a business, a non-profit, 
or another type of organization]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""

from functions import url_categorize

url = str(input("Enter url surfix: "))

url_type = url_categorize(url)

print()
print(f"{url_type}")
