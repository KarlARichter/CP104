"""
-------------------------------------------------------
[Functions.py / Lab04]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""

import math


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)   
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    diam = 2 * radius
    return diam


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sh = math.sqrt((base/2)**2 + height**2)

    area = (base**2) + 2 * base * (math.sqrt(((base**2)/4) + height ** 2))

    vol = base**2 * (height/3)

    return sh, area, vol


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    NICKELS = 0.05
    DIMES = 0.10
    QUARTERS = 0.25
    LOONIES = 1.00
    TOONIES = 2.00

    total = (NICKELS * nickels) + (DIMES * dimes) + (QUARTERS *
                                                     quarters) + (LOONIES * loonies) + (TOONIES * toonies)
    return total


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """

    DAYS = 365
    HOURS = 24
    SECONDS = 60
    SECONDS_2 = 60

    SECONDS_YEAR = DAYS * HOURS * SECONDS * SECONDS_2

    births = SECONDS_YEAR / births
    deaths = SECONDS_YEAR / deaths
    immigrants = SECONDS_YEAR / immigrants

    annual_change = births - deaths + immigrants

    new_size = size + (annual_change * years)

    return int(new_size)


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """

    DAYS = seconds // 86400

    HOURS = seconds // 3600

    MINUTES = seconds // 60

    return DAYS, HOURS, MINUTES


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """

    DAYS = initial_seconds // 86400
    REMAINING_SECONDS = initial_seconds % 86400

    HOURS = REMAINING_SECONDS // 3600
    REMAINING_SECONDS %= 3600

    MINUTES = REMAINING_SECONDS // 60
    SECONDS = REMAINING_SECONDS % 60

    return DAYS, HOURS, MINUTES, SECONDS
