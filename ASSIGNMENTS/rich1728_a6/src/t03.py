"""
-------------------------------------------------------
[Prints a table of monthly interest and payments on a loan]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
from functions import interest_table


principal_amount = float(input("Enter the original value of the loan: "))
interest_rate = float(input("Enter yearly interest rate (%): "))
payment = float(input("Enter the monthly payments: "))


interest_table(principal_amount, interest_rate, payment)
