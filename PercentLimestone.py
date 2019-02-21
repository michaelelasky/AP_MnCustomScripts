# Author(s) Jeanette Gowen
# Date 5/29/2018
# Title PercentLimestone
# Used to calculate Percent Limestone
# Code version 1.00
# Type (Python Custom Module)

def calcpercentLimestone(percentCO2Cement, percentCO2Limestone):
	roundperLimestone = None
	if percentCO2Cement and percentCO2Limestone:
		percentLimestone = (percentCO2Cement / percentCO2Limestone) * 100
		roundperLimestone = round(percentLimestone, 1)
	return roundperLimestone

