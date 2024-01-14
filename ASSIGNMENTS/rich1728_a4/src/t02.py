"""
-------------------------------------------------------
[Returns the pollution level given an AQI 
(Air Quality Index)]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""

from functions import pollution_ranking

air_quality_index = int(input("Enter Air Quality Index(AQI): "))
pollution = pollution_ranking(air_quality_index)

print()
print(f"{air_quality_index} AQI falls under the following category: {pollution}")
