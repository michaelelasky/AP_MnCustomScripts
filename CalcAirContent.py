# Author(s) Mike Elasky
# Date 12/20/2018
# Title CalcAirContent
# used to calculate air content
# Code version 1.00
# Type (Python Custom Module)

def calcairContent(reportedspg = None, airwater = None, wtmortar = None):
	aircontent = None
	if reportedspg is not None and airwater is not None and wtmortar is not None:
		if ((reportedspg < 3.10 or  reportedspg > 3.20)  and (airwater <> -1750)):
			aircontent =  round(100*(1-(wtmortar/400)/((1750+airwater)/((350/ reportedspg)+(1400/2.65)+airwater))), 1)
		else:
			airfactor = (airwater/350)*100
			aircontent = round(100-(wtmortar*(182.7+(airfactor))/(2000+(4*airfactor))), 1)
	return aircontent