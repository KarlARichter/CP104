"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌‌​‌​‌‌​​​​​:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    vowels = "aeiouAEIOU"
    altered = ""

    for char in string:
        if char.isalpha():
            altered += char.upper() if char in vowels else char.lower()
        else:
            altered += char

    return altered
