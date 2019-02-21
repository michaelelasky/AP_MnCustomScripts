# Author(s) Michael Elasky
# Date 4/27/2018
# Title InOutOfTolerance
# Used to calculate weight of previous sieve
# Code version 1.00
# Type (Python Custom Module)

def inoutofTolerance(labfieldtolerance=None, labcrushed=None):
	intolerance = None
	if labfieldtolerance and labcrushed:
		if labfieldtolerance > (labcrushed + 15) or labfieldtolerance < (labcrushed - 15):
			intolerance = 'Out of Tolerance'
		intolerance = 'In Tolerance'
	return intolerance