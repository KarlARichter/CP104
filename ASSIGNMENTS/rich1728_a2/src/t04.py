"""
-------------------------------------------------------
[This program divides a number of flyers evenly amongst 
delivery people for distribution]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

flyers = int(input("Number of flyers: "))
delivery = int(input("Number of delivery people: "))

flyer_person = flyers // delivery
flyers_left = flyers % delivery

print()
print(f"Flyers per delivery person: {flyer_person}")
print(f"Flyers left over: {flyers_left}")
