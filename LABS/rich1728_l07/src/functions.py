"""
-------------------------------------------------------
[Lab 7 - functions.py]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    while target > current:
        current += (current * rate / 100)
        years += 1
    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """

    minimum = float('inf')
    maximum = float('-inf')
    total = 0.0
    count = 0

    while True:
        value = float(input("Next positive value: "))

        if value < 0:
            break

        if count == 0:
            minimum = maximum = value

        minimum = min(minimum, value)
        maximum = max(maximum, value)
        total += value
        count += 1

    if count == 0:
        minimum = maximum = total = average = 0.0
    else:
        average = total / count

    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """

    expenses = 0.0

    while True:
        expense = float(input("Enter an expense (0 to quit): $"))

        if expense == 0:
            break

        expenses += expense

    balance = available - expenses

    if balance > 0:
        status = 'Surplus'
    elif balance < 0:
        status = 'Deficit'
    else:
        status = 'Balanced'

    return expenses, balance, status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """

    while high > low:
        value = int(input(f"Enter a value between {low} and {high}: "))
        if low <= value <= high:
            break
        elif value > high:
            print("Value entered is too high")
        else:
            print("Value entered is too low")

    while low > high:
        value = "'High' number must be larger than 'low' number"
        break

    return value


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    OVERTIME_RATE = 1.5
    TAX = 0.03625
    OVERTIME = 40

    total_wages = 0
    count = 0

    while True:
        employee_id = int(input("Enter employee ID (0 to quit): "))
        if employee_id == 0:
            break

        hourly_rate = float(input("Enter your hourly wage rate: "))
        hours_worked = float(input("Enter your number of hours worked: "))

        if hours_worked > OVERTIME:
            regular_wages = OVERTIME * hourly_rate
            overtime_wages = (hours_worked - OVERTIME) * \
                hourly_rate * OVERTIME_RATE
            amount_wages = regular_wages + overtime_wages
        else:
            amount_wages = hours_worked * hourly_rate

        net_wages = amount_wages - (amount_wages * TAX)

        print(f"Net payment for employee {employee_id}: ${net_wages:,.2f}")
        print()
        total_wages += net_wages
        count += 1

    if count == 0:
        total_wages, average_wages = 0, 0
    else:
        average_wages = total_wages / count

    return total_wages, average_wages
