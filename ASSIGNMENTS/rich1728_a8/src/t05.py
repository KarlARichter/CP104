"""
------------------------------------------------------------------------
[Determines if a list of strings is a word chain.]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-10-21"
------------------------------------------------------------------------
"""

from functions import has_word_chain
words_inp = str(input("Enter words: "))

words = words_inp.split()

word_chain = has_word_chain(words)

print()
print(f"{word_chain}")