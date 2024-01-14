"""
------------------------------------------------------------------------
[Returns the longest common ending of two strings]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-10-21"
------------------------------------------------------------------------
"""

from functions import common_end

str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))

suffix = common_end(str1, str2)

print()
print(f"{suffix}")