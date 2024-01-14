"""
-------------------------------------------------------
[Assingment 06 - functions.py]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""


def total_wins():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings representing 
    game outcomes and counts how many times "purple" and "gold" 
    appeared in the input.
    Use: total_wins()
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        purple_count (int) - The number of times "purple" appeared in the input.
        gold_count (int) - The number of times "gold" appeared in the input.    
    ------------------------------------------------------
    """
    purple_count = 0
    gold_count = 0

    while True:
        winning_team = input(
            "Enter the winning team (or press Enter to finish): ").strip().lower()
        if not winning_team:
            break
        elif winning_team == "purple":
            purple_count += 1
        elif winning_team == "gold":
            gold_count += 1

    return purple_count, gold_count


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    if number <= 1:
        prime = False
    elif number <= 3:
        prime = True
    elif number % 2 == 0 or number % 3 == 0:
        prime = False
    else:
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                prime = False
                break
            i += 6
        else:
            prime = True

    return prime


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """

    number = abs(number)
    digits = 0
    while number != 0:
        digits = digits + 1
        number = number // 10
    return digits


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    monthly_interest_rate = interest_rate / 100 / 12
    month = 1

    print()
    print(f"principal_amount: ${principal_amount:.2f}")
    print(f"Interest rate: {interest_rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while principal_amount > 0:
        monthly_interest = principal_amount * monthly_interest_rate
        if principal_amount < payment:
            payment = principal_amount + monthly_interest
            principal_amount = 0
        else:
            principal_amount -= payment - monthly_interest
        print(
            f"{month:>5}    {monthly_interest:>2.2f}    {payment:>5.2f}    {principal_amount:>7.2f}")
        month += 1
    return


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """

    total = 0
    factor = 1
    while number != 0 and factor < number:
        if number % factor == 0:
            total = total + factor
            factor = factor + 1
        else:
            factor = factor + 1
    return total
