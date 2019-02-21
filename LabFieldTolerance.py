# Author(s) Mike Elasky
# Date 01/13/2018
# Title LabFieldTolerance
# used to calc the toleranc between field and lab gradation values
# Code version 2.00
# Type (Python Custom Module)

def calclabfieldTolerance(lab=None,field=None):
	tolerance = None
	if lab and field:
		tolerance = lab - field
		tolerance = round (tolerance, 0)
	return tolerance