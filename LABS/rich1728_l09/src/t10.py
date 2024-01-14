"""
-------------------------------------------------------
[Analyzes txt and returns the number of uppercase letters,
lowercase letters, digits, and number of whitespaces in txt]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""

from functions import text_analyze

txt = str(input("Enter sentence: "))

uppr, lowr, dgts, whtspc = text_analyze(txt)

print()
print(f"{uppr}, {lowr}, {dgts}, {whtspc}")
