# Author(s) Michael Elasky
# Date 2/23/18
# Title of program-SpecificationRange
# Used for creating a specification range measage
# Code version 1.00
# Type (Python Custom Module)

def specificationRange(targetvalue=None,positivetargetdeviation=None,negativetargetdeviation=None):
	if targetvalue and positivetargetdeviation and negativetargetdeviation:
		min = targetvalue - negativetargetdeviation
		max = targetvalue + positivetargetdeviation
		minmaxrange = str(min) + ' - ' + str(max)
	elif not targetvalue or not positivetargetdeviation or not negativetargetdeviation:
		return
	else:
		 minmaxrange = 'No pec range'
	return minmaxrange