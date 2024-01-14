"""
-------------------------------------------------------
[This program asks the user to enter a positive two-digit integer. 
The program then prints the difference of the two digits.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

num1 = int(input("Enter a positive digit number: "))

digit_1 = num1 // 10
digit_2 = num1 % 10

difference = digit_1 - digit_2

print()
print(f"The difference of the digits of {num1} is {difference}")
