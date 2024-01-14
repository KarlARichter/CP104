"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_i    n - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌‌​‌​‌‌​​​​​:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    matrix = []

    for _ in range(rows):
        row_values = fh_in.readline().split()
        row_values = [int(value) if value.isdigit()
                      else 0 for value in row_values]
        row_values = row_values[:cols] + [0] * (cols - len(row_values))
        matrix.append(row_values)

    return matrix
