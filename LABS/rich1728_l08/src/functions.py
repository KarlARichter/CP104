"""
-------------------------------------------------------
[functions.py // rich1728_l8]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
from random import randint


def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """

    name = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    return name[m - 1]


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """

    numbers = set()
    while len(numbers) < n:
        numbers.add(randint(low, high))

    return sorted(list(numbers))


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """

    values = [int(value) for value in values]

    negatives = sum(1 for value in values if value < 0)
    positives = sum(1 for value in values if value > 0)
    zeroes = sum(1 for value in values if value == 0)
    evens = sum(1 for value in values if value % 2 == 0)
    odds = sum(1 for value in values if value % 2 != 0)

    return negatives, positives, zeroes, evens, odds


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    indexes = []
    for i in range(len(values)):
        if values[i] == value:
            indexes.append(i)
    return indexes


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """

    source1 = [float(x) for x in source1]
    source2 = [float(x) for x in source2]
    target = [a+b for a, b in zip(source1, source2)]
    return target
