"""
-------------------------------------------------------
[This program calculate a students final grade by inputting their
midterm and final grade with respective percentages.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

Midterm = float(input("Midterm mark (%): "))
Exam = float(input(" Exam mark (%): "))

MIDTERM_PERCENTAGE = 0.35
EXAM_PERCENTAGE = 0.65

final = (Midterm * MIDTERM_PERCENTAGE) + (Exam * EXAM_PERCENTAGE)
print("Final Grade (%):", final)
