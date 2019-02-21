# Author(s) Jeanette Gowen
# Date 5/29/2018
# Title PercentCO2
# Used to calculate Percent CO2
# Code version 1.00
# Type (Python Custom Module)

def calcpercentCO2(loitareWeight, loisampleWeight, loiignitionwt550, loiignitionwt950):
	roundperCO2 = None
	if loitareWeight and loisampleWeight and loiignitionwt550 and loiignitionwt950:
		percentCO2 = ((loiignitionwt550 - loiignitionwt950)/(loisampleWeight - loitareWeight)) * 100
		roundperCO2 = round(percentCO2, 2)
	return roundperCO2


