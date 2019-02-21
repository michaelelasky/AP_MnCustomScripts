# Author(s) Michael Elasky
# Date 5/7/2018
# Title SPGByFlask
# Used to calculate SPG by Flask
# Code version 1.00
# Type (Python Custom Module)

def getspgbyFlask(cementWt, reading2, reading1):
	spgbyFlask = None
	if cementWt and reading2 and reading1:
		spgbyFlask = cementWt / (reading2 - reading1)
	return spgbyFlask