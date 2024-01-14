"""
-------------------------------------------------------
Midterm B Task 4 Testing
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
from t04_functions import get_it

response =  str(input("Enter response to be classified: "))

classification = get_it(response)

print(f"The response '{response}' is classified under: {classification}")