"""
-------------------------------------------------------
[LAB 5 - Functions.py]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """

    GRAVITY = 9.8
    weight = GRAVITY * mass

    if weight > 1000:
        message = "heavy"
    elif weight < 10:
        message = "light"
    else:
        message = "average"

    return weight, message


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    distance_v1 = abs(target - v1)
    distance_v2 = abs(target - v2)

    if distance_v1 <= distance_v2:
        result = v1
    else:
        result = v2

    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    if speed in range(1, 39):
        category = "Breeze"
    elif speed in range(39, 62):
        category = "Strong Wind"
    elif speed in range(62, 89):
        category = "Gale Winds"
    elif speed in range(89, 118):
        category = "Whole Gale"
    elif speed >= 118:
        category = "Hurricane"
    else:
        category = "Unknown"
    return category


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Parameters:
        SALARY - constant set to 30000
        YEARS - constant set to 5
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    SALARY = 30000
    YEARS = 5

    year_input = int(input("Enter years worked: "))

    qualified = False

    if year_input >= YEARS:
        salary_input = int(input("Enter yearly salary: "))
        if salary_input >= SALARY:
            qualified = True
        else:
            print("Must have minimum salary 30000")
    else:
        print("Must work minimum 4 years")
    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Parameters:
        make_combo - determines if combo is true or false
        order - determines order
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00

    order = input("Order B - burger or W - wings: ").upper()
    make_combo = input("Make it a combo? (Y/N): ").upper()

    if make_combo == "Y":
        side_order = input("Add F - fries or S - salad: ").upper()
        if order == "B":
            if side_order == "F":
                price = BURGER + FRIES
            elif side_order == "S":
                price = BURGER + SALAD
        elif order == "W":
            if side_order == "F":
                price = WINGS + FRIES
            elif side_order == "S":
                price = WINGS + SALAD
    else:
        if order == "B":
            price = BURGER
        elif order == "W":
            price = WINGS
        else:
            price = 0
    return price
