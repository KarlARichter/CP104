"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""

BASE_COST = 125
COST_EXTRA = 25
VIP_DISC = 0.1

def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌‌​‌​‌‌​​​​​:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    extra_services = int(input("How many extra services are you purchasing? "))
    vip = str(input("Are you a VIP member (Y/N)? ")) == "Y"

    cost = BASE_COST + extra_services * COST_EXTRA

    if extra_services > 1:
        if vip:
            cost -= cost * VIP_DISC
    return cost
