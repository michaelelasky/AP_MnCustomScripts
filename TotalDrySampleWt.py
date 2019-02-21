# Author(s) Michael Elasky
# Date 07/09/2018
# Title TotalDrySampleWt
# used to calculate Total Dry Sample Weight
# Code version 1.00
# Type (Python Custom Module)

def totaldrysampleWt(totalwtdrycoarse = None, totalwtdryfine = None):
	totaldrysamplewt = None
	if totalwtdrycoarse and totalwtdryfine:
		totaldrysamplewt = totalwtdrycoarse + totalwtdryfine
	return totaldrysamplewt