# Author(s) Michael Elasky
# Date 07/11/2018
# Title WtPassing
# used to calculate Total Weight Passing
# Code version 1.00
# Type (Python Custom Module)

def wtPassing(wtprevious = None, wtretained = None):
	wtpassing = None
	if wtprevious and wtretained:
		wtpassing = wtprevious - float(wtretained)
	return wtpassing