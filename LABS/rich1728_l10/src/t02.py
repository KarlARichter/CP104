"""
-------------------------------------------------------
[Find the record for a given ID in a sequential file.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
from functions import customer_by_id

fh = open("customers.txt", "r", encoding="utf-8")
id_number = input("Find customer by id_number\nEnter an ID: ")
result = customer_by_id(fh, id_number)
print()
print(result)
