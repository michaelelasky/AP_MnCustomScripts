# Author(s) Jeanette Gowen
# Date 6/11/2018
# Title PercentCO2Limestone
# Used to calculate Percent CO2 Limestone
# Code version 1.00
# Type (Python Custom Module)

def calcpercentCO2Limestone(caCO3pct):
	roundperCO2Limestone = None
	if caCO3pct:
		percentCO2Limestone = caCO3pct/2.274
		roundperCO2Limestone = round(percentCO2Limestone, 2)
	return roundperCO2Limestone


