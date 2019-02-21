# Author(s) Michael Elasky
# Date 4/27/2018
# Title PercentMoisture
# Used to calculate Percent Moisture
# Code version 1.00
# Type (Python Custom Module)

def calcpercentMoisture(loisampleWeight, loiignitionwt110, loitareWeight):
	roundperMoisture = None
	if loisampleWeight and loiignitionwt110 and loitareWeight:
		try:
			percentMoisture = ((loisampleWeight - loiignitionwt110)/(loisampleWeight - loitareWeight))*100
			roundperMoisture = round(percentMoisture, 1)
		except ZeroDivisionError:
			return True
		else:
			return roundperMoisture