"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
LOONIE = 100
QUARTER = 25
DIME = 10
NICKEL = 5

def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌‌​‌​‌‌​​​​​:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """
    
    loonies = cents // LOONIE
    cents %= LOONIE

    quarters = cents // QUARTER
    cents %= QUARTER

    dimes = cents // DIME
    cents %= DIME

    nickels = cents // NICKEL

    return loonies, quarters, dimes, nickels
