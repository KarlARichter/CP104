"""
-------------------------------------------------------
[Calculates and returns the weekly employee payroll for 
all employees in an organization.]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
from functions import employee_payroll

total, average = employee_payroll()

print()
print(f"Total net employee wages: ${total:,.2f}")
print(f"Average employee net wages: ${average:,.2f}")
