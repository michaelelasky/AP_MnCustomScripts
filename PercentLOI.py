# Author(s) Michael Elasky
# Date 4/27/2018
# Title PercentLOI
# Used to calculate Percent LOI
# Code version 1.00
# Type (Python Custom Module)

def calcpercentLOI(loiignitionwt110, loiignitionwt750, loitareWeight):
	roundperLOI = None
	if loiignitionwt110 and loiignitionwt750 and loitareWeight:
		try:
			percentLOI = ((loiignitionwt110 - loiignitionwt750)*100/(loiignitionwt110 - loitareWeight))
			roundperLOI = round(percentLOI, 1)
		except ZeroDivisionError:
			return True
		else:
			return roundperLOI