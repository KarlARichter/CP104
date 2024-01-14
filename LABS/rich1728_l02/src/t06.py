"""
-------------------------------------------------------
[Calculates the monthly payment for a mortgage]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""

pincipal = float(input("Mortgage principal ($): "))
numPayments = int(input("Number of years: "))
interest = float(input("Yearly interest rate (%): "))

interest_year = (interest / 12) / 100
numPayments_year = numPayments * 12

payments = pincipal * \
    ((interest_year*(1 + interest_year)**numPayments_year) /
     ((1 + interest_year)**numPayments_year - 1))

print("\nThe monthly payments are: $", payments)
