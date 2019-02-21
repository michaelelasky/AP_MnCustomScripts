# Author(s) Mike Elasky
# Date 02/19/2019
# Title UsedSpG
# Used to find SpG if there is no entered SpG
# Code version 1.00
# Type (Python Custom Module)

def usedSpG(spgHelium)
	usedspg = None
	if spgHelium:
		usedspg = spgHelium
	else:
		usedspg = 2.65
	return usedspg