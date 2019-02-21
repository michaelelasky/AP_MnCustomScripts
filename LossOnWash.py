# Author(s) Michael Elasky
# Date 07/09/2018
# Title LossOnWash
# used to calculate Loss On Wash
# Code version 1.00
# Type (Python Custom Module)

def lossonWash(wtbeforewash = None, wtafterwash = None):
	lossonwash = None
	if wtbeforewash and wtafterwash:
		lossonwash = wtbeforewash - wtafterwash
	return lossonwash