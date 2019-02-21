# Author(s) Michael Elasky
# Date 5/7/2018
# Title CementAdded
# Used to calculate Cement Added
# Code version 1.00
# Type (Python Custom Module)

def getcementAdded(flaskwt2, flaskwt1):
	cementAdded = None
	if flaskwt2 and flaskwt1:
		cementAdded = flaskwt2 - flaskwt1
	return cementAdded