"""
-------------------------------------------------------
[Functions.py // Lab06]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = char * (2 * i - 1)
        print(spaces + stars)
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(n, 0, -1):
        bottles = "bottle" if i == 1 else "bottles"
        next_bottles = "bottle" if i - 1 == 1 else "bottles"

        print(f"{i} {bottles} of beer on the wall, {i} {bottles} of beer.")
        print(
            f"Take one down, pass it around, {i-1 if i > 1 else 'no more'} {next_bottles} of beer on the wall!")
    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print()
    print("Age         Salary")
    print("------------------")
    for year in range(age, 66):
        print(f"{year}       {salary:>9,.2f}")
        salary += salary * (increase / 100)
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    minimum = float('inf')
    maximum = float('-inf')
    total = 0
    count = 0

    for i in range(n):
        if i == 0:
            prompt = "First value: "
        else:
            prompt = "Next value: "
        value = float(input(prompt))
        total += value
        count += 1
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    if count > 0:
        average = total / count
    else:
        average = 0

    return minimum, maximum, total, average
