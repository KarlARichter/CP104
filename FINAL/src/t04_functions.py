"""
-------------------------------------------------------
Exam Task 4 Function Definitions
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def draw_x(height):
    """
    -------------------------------------------------------
    Prints a X shape height characters high.
    Use: draw_x(height)
    -------------------------------------------------------
    Parameters:
        height - maximum height in characters of X shape (int >= 3)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌‌​‌​‌‌​​​​​:
        None
    -------------------------------------------------------
    """

    if height % 2 == 0:
        height += 1

    for i in range(height):
        for j in range(height):
            if i == j or i + j == height - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    return
