# Author(s) Michael Elasky
# Date 4/27/2018
# Title SievesRatio
# Used to calculate ratio of percent passing
# Code version 1.00
# Type (Python Custom Module)

def sievesRatio(PctPassingA = None,PctPassingB = None):
	ratio = None
	if PctPassingA and PctPassingB:
		try:
			ratio = round(((PctPassingA / PctPassingB)*100),2)
		except ZeroDivisionError:
			return True
		else:
			return ratio
	