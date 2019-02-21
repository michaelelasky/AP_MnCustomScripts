# Author(s) Michael Elasky
# Date 07/09/2018
# Title TotalWt
# used to calculate Total Weight
# Code version 1.00
# Type (Python Custom Module)

def calctotalWeight(wt2facedcrushed = None,wt1facedcrushed = None,wtnoncrushed = None):
	totalwt = None
	if wt2facedcrushed and wt1facedcrushed and wtnoncrushed:
		totalwt = wt2facedcrushed + wt1facedcrushed + wtnoncrushed
	return totalwt