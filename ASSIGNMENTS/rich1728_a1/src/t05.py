"""
------------------------------------------------------------------------
[This program allows the user to enter various data in order to calculate 
their the balance of their compound interest]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-09-18"
------------------------------------------------------------------------
"""


principal = float(input("Principal: "))
interest = float(input("Interest (%): "))
numYears = int(input("Number of years: "))
numTimes = int(input("Number of times interest compounded per year: "))

interest_percent = interest / 100

balance = principal * (1 + interest_percent /
                       numTimes) ** (numTimes * numYears)

print(balance)
