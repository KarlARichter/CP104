"""
-------------------------------------------------------
[Prints a table of the number of calories burned every 
five minutes given the number of calories burned per minute 
an the total number of minutes run]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-24"
-------------------------------------------------------
"""

from functions import calories_treadmill

per_min = float(input("Enter amount of calories burnt per minute: "))
minutes = int(input("Enter amount of time ran: "))

result_table = calories_treadmill(per_min, minutes)
