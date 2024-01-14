"""
-------------------------------------------------------
[functions.py // Lab11]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """

    rows = len(matrix)
    cols = len(matrix[0])
    print("", end="")
    for i in range(cols):
        print("{:7}".format(i), end="")
    print()
    for row in range(rows):
        print("{:2}".format(row), end="")
        for coloumn in range(cols):
            if value_type == "float":
                print("{:7.2f}".format(matrix[row][coloumn]), end="")
            if value_type == "int":
                print("{:7}".format(matrix[row][coloumn]), end="")
    print()
    return


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """

    print(" ", end="")
    for x in range(len(matrix[0])):
        print("{:>5d}".format(x), end="")
    print()
    for x in range(len(matrix)):
        print("{:>2.0f}".format(x), end=""
              )
        for y in range(len(matrix[x])):
            print("{:>5s}".format(matrix[x][y], end=""))
        print()
    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0

    for i in range(num_rows):
        for j in range(num_cols):
            current_value = matrix[i][j]

            total += current_value

            if current_value < smallest:
                smallest = current_value

            if current_value > largest:
                largest = current_value

    average = total / (num_rows * num_cols)

    return smallest, largest, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    min_value = matrix[0][0]
    max_value = matrix[0][0]
    s_loc = [0, 0]
    l_loc = [0, 0]

    for i in range(num_rows):
        for j in range(num_cols):
            current_value = matrix[i][j]

            if current_value < min_value:
                min_value = current_value
                s_loc = [i, j]

            if current_value > max_value:
                max_value = current_value
                l_loc = [i, j]

    return s_loc, l_loc


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
