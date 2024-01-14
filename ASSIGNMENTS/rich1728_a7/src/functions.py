"""
-------------------------------------------------------
[functions.py // Assignment07]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""


def list_factors(number):
    """
    -------------------------------------------------------
    [This function takes an integer greater than 0 as a parameter 
    and returns a list of the factors that make up that number 
    excepting the number itself. An integer's factors are the 
    whole numbers that the integer can be evenly divided by.]
    use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
       number - number user inputs (int)
    Returns:
       factors - factors number is divided by (int)
    -------------------------------------------------------
    """

    factors = []

    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    number_list = []
    while True:
        num = int(input("Enter a positive number: "))
        if num > 0:
            number_list.append(num)
        elif num == 0:
            break
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []

    for i in range(len(numbers)):
        if numbers[i] == target_number:
            index_list.append(i)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    indexes_to_remove = [i for i, value in enumerate(
        minuend) if value in subtrahend]

    for i in reversed(indexes_to_remove):
        minuend.pop(i)
    return


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            in_order = False
            index = i
            break

    return in_order, index
