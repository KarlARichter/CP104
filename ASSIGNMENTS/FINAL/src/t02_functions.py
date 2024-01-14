"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
DRY_THRESHOLD = 4
WET_THRESHOLD = 8
SENTINEL_VALUE = -1

dry_days = 0
damp_days = 0
wet_days = 0
total_rainfall = 0
day_count = 0


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌‌​‌​‌‌​​​​​:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    while True:
        rainfall_input = int(input("Rainfall mm (-1 to stop): "))

        if rainfall_input == SENTINEL_VALUE:
            break

        day_count += 1
        total_rainfall += rainfall_input

        if rainfall_input < DRY_THRESHOLD:
            dry_days += 1
        elif DRY_THRESHOLD <= rainfall_input <= WET_THRESHOLD:
            damp_days += 1
        else:
            wet_days += 1

    if day_count == 0:
        avg = 0
    else:
        avg = total_rainfall // day_count

    return dry_days, damp_days, wet_days, avg
