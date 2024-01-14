"""
-------------------------------------------------------
[This program calculates the annual tax paid by a company]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

sale = int(input("Enter the total sales: "))
TAX_RATE = 18.50
tax = (sale * TAX_RATE)/100

print()
print("Projected Tax Report")
print(f"--------------------------")
print(f"Total sales:   $ {sale:,.2f}")
print(f"Annual tax:    % {TAX_RATE:.2f}")
print("--------------------------")
print(f"Tax:           $ {tax:,.2f}")
