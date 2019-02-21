# Author(s) Michael Elasky
# Date 5/17/2018
# Title TimeOfSet
# Used to calculate Initial and Final Time of Set
# Code version 1.00
# Type (Python Custom Module)

def timeofSet(hr, min, starthr, startmin):
	time = None
	if hr is not None and min is not None and starthr is not None and startmin is not None:
		time =round((( hr + min /60)-( starthr + startmin /60))*60)
	return time