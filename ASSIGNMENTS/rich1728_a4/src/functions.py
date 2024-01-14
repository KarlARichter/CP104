"""
-------------------------------------------------------
[rich1728_a4 - functions.py]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is Sunday, day 7 is Saturday.
    Returns Error if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """

    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]

    if 1 <= day_num <= 7:
        day = days[day_num - 1]
    else:
        day = "Error"

    return day


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        Good - 0 to 50 AQI
        Moderate - 51 - 100 AQI
        Unhealthy for Sensitive Groups - 101 - 150 AQI
        Unhealthy - 151 - 200 AQI
        Very Unhealthy - 201 - 300 AQI
        Hazardous - 300+ AQI
    Returns Error if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """

    if air_quality_index in range(1, 50):
        pollution = "Good"
    elif air_quality_index in range(51, 100):
        pollution = "Moderate"
    elif air_quality_index in range(101, 150):
        pollution = "Unhealthy for Sensitive Groups"
    elif air_quality_index in range(151, 200):
        pollution = "Unhealthy"
    elif air_quality_index in range(201, 300):
        pollution = "Very Unhealthy"
    elif air_quality_index >= 300:
        pollution = "Hazardous"
    else:
        pollution = "Error"
    return pollution


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1 >= val2 and val1 >= val3:
        largest = val1
        if val2 >= val3:
            second_largest = val2
        else:
            second_largest = val3
    elif val2 >= val1 and val2 >= val3:
        largest = val2
        if val1 >= val3:
            second_largest = val1
        else:
            second_largest = val3
    else:
        largest = val3
        if val1 >= val2:
            second_largest = val1
        else:
            second_largest = val2
    average = (largest + second_largest) / 2
    return average


def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """

    color_pairs = {
        ("red", "blue"): "fuchsia",
        ("red", "green"): "yellow",
        ("green", "blue"): "aqua",
        ("red", "red"): "red",
        ("blue", "blue"): "blue",
        ("green", "green"): "green",
    }

    rgb_colour1 = rgb_colour1.lower()
    rgb_colour2 = rgb_colour2.lower()

    if (rgb_colour1, rgb_colour2) in color_pairs:
        rgb_colour = color_pairs[(rgb_colour1, rgb_colour2)]
    elif (rgb_colour2, rgb_colour1) in color_pairs:
        rgb_colour = color_pairs[(rgb_colour2, rgb_colour1)]
    else:
        rgb_colour = "Error"

    return rgb_colour


def hoo_rah(number):
    """
    -------------------------------------------------------
    Returns a statement depending on number entered:
        "Hoo" - if number is evenly divisible by 2
        "Rah" - if number is evenly divisible by 7
        "Hoo Rah" if number is evenly divisible by both 2 and 7
    Returns Zip if number is none of the above
    Use: sentence = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - Number inputed by user (int)
    Returns:
        sentence - name of string (str)
    ------------------------------------------------------
    """

    if number % 2 == 0 and number % 7 == 0:
        sentence = "Hoo Rah"
    elif number % 2 == 0:
        sentence = "Hoo"
    elif number % 7 == 0:
        sentence = "Rah"
    else:
        sentence = "Zip"
    return sentence
