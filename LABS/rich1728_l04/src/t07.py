"""
-------------------------------------------------------
[Calculates the total value of a set of coins in dollars]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""


from functions import total_change

n = int(input("Enter amount of nickels: "))
d = int(input("Enter amount of dimes: "))
q = int(input("Enter amount of quarters: "))
l = int(input("Enter amount of loonies: "))
t = int(input("Enter amount of toonies: "))

total = total_change(n, d, q, l, t)

print(f"\nTotal amount of money: ${total:.2f}")
