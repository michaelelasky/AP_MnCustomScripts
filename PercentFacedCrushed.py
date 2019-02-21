# Author(s) Mike Elasky
# Date 01/13/2018
# Title PercentFacedCrushed
# used to calc the percent faced crushed
# Code version 2.00
# Type (Python Custom Module)

def calcperfacedCrushed(wt2facedcrushed = None,wt1facedcrushed = None,totalwt = None):
	perfacedcrushed = None
	if wt2facedcrushed and wt1facedcrushed and totalwt:
		perfacedcrushed = ((wt2facedcrushed + wt1facedcrushed) / totalwt)* 100
		perfacedcrushed = round (perfacedcrushed, 0)
	elif wt2facedcrushed and wt1facedcrushed:
		perfacedcrushed = (wt2facedcrushed + wt1facedcrushed)* 100
		perfacedcrushed = round (perfacedcrushed, 0)
	return perfacedcrushed
		