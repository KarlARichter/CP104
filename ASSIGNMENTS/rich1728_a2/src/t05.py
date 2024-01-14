"""
-------------------------------------------------------
[This tests program prompts the user for the size of the 
shed foundation, height of its walls, the cost of concrete 
per m^3, and the cost of bricks per m^2, and calculate and 
print the amount of concrete and bricks needed, and the 
total cost of the materials.]
-------------------------------------------------------
Author:  Karl Richter
ID:      169061728
Email:   rich1728@wlu.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""
# INPUTS:
found_LENGTH = float(input("Foundation length (m): "))
found_WIDTH = float(input("Foundation width (m): "))
found_HEIGHT = float(input("Foundation height (m): "))
wall_HEIGHT = float(input("Wall height (m): "))
concrete_COST = float(input("Cost of concrete ($/m^3): "))
bricks_COST = float(input("Cost of bricks ($/m^2): "))

# CALCULATIONS:
found_PRICE = found_LENGTH * found_WIDTH * found_HEIGHT
concrete_PRICE = found_PRICE * concrete_COST
bricks_NEEDED = 2 * ((found_LENGTH * wall_HEIGHT) +
                     (found_WIDTH * wall_HEIGHT))
bricks_PRICE = bricks_NEEDED * bricks_COST
TOTAL_PRICE = concrete_PRICE + bricks_PRICE

# OUTPUTS:
print()
print(f"Concrete needed for foundation (m^3): {found_PRICE:.2f}")
print(f"Cost of concrete: ${concrete_PRICE:.2f}")
print(f"Bricks needed for walls (m^2): {bricks_NEEDED:.2f}")
print(f"Cost of bricks: ${bricks_PRICE:,.2f}")
print(f"Total cost: ${TOTAL_PRICE:,.2f}")
