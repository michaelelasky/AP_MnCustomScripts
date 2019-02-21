# Author(s) Mike Elasky
# Date 12/24/2018
# Title CalcAirPropFactor
# used to calculate air prop factor
# Code version 1.00
# Type (Python Custom Module)

def airpropFactor(airwater = None):
	airpropfactor = None
	if airwater:
		airfactor = (airwater/350)*100
		airpropfactor = round((182.7 + airfactor) / (2000 + (4 * airfactor)), 5)
	return airpropfactor