# Author(s) Mike Elasky
# Date 01/13/2018
# Title PctPassing
# used to calc the percent passing sieves
# Code version 2.00
# Type (Python Custom Module)

def pctPassing(wtprevious=None, wtretained=None, totaldrysamplewt=None, wtbeforewash=None, totalwtdryfine=None, sievesize=None, iscoarseflag=None):
	pctpassing = None
	if wtprevious and wtretained:
		if totaldrysamplewt and iscoarseflag == 1:
			pctpassing = round(((wtprevious - float(wtretained)) / totaldrysamplewt * 100), 1)
		elif wtbeforewash and totalwtdryfine and totaldrysamplewt and iscoarseflag == 0:
			if sievesize == 'Bottom Pan (F)' or sievesize == 'Bottom Pan (C)':
				pctpassing = 0.0
			else:
				finepasspct = ((wtprevious - float(wtretained)) / wtbeforewash * 100)
				finepct = (totalwtdryfine / totaldrysamplewt)
				pctpassing = round((finepasspct * finepct), 1)
	return pctpassing
	