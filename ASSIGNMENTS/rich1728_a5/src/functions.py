"""
-------------------------------------------------------
[Functions.py // Assignment 5]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-24"
-------------------------------------------------------
"""


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    product = 1
    for i in range(2, number + 1):
        product *= i
    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every 
    five minutes given the number of calories burned per minute 
    an the total number of minutes run
    Use:  = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min = number of calories burnt per minute (int)
        minutes = amount of time ran (float)
    Returns:
        None
    ------------------------------------------------------
    """
    print()
    for i in range(5, minutes + 1, 5):
        calories_burned = i * per_min
        print(f"{i:3}  {calories_burned:5.1f}")

    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    takes an integer parameter and prints a arrow of # characters pointing up
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows of # to print (int) 
    Returns:
        None
    ------------------------------------------------------
    """
    print()
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        if i == 0:
            print(spaces + "#")
        else:
            print(spaces + "#" + " " * (2 * i - 1) + "#")

    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print()
    print(" " * 4, end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:4d}", end="")
    print()
    print("-" * 27)

    for i in range(start_num, stop_num + 1):
        print(f"{i:2d} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:4d}", end="")
        print("")

    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    end = start + (increment * count)
    total = 0

    for i in range(start, end, increment):
        total += i
    return total
