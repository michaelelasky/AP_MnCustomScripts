# Author(s) Jeanette Gowe n
# Date 06/07/2018
# Title PercentLOIChemCE
# Used to calculate Percent LOI for Chem Analysis for CE
# Code version 1.00
# Type (Python Custom Module)

def calcpercentLOI(loisamplewt, loiignitionwt950, loitareWeight):
	roundperLOI = None
	if loisamplewt and loiignitionwt950 and loitareWeight:
		percentLOI = ((loisamplewt - loiignitionwt950)*100/(loisamplewt - loitareWeight))
		roundperLOI = round(percentLOI, 1)
	return roundperLOI

