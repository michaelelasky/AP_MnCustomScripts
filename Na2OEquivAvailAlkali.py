# Author(s) Michael Elasky
# Date 4/27/2018
# Title Na2OEquivAvailAlkali
# Used to calculate Na2O Equivalent Available Alkali or Na2O Equiv. Tot. Alkali.
# Code version 1.00
# Type (Python Custom Module)

def calcna2OequivavailAlkali(availna2Oper, availk2Oper):
	roundna2Oequivavailalkali = None
	if availna2Oper and availk2Oper:
		na2Oequivavailalkali = availna2Oper + (0.658 * availk2Oper)
		roundna2Oequivavailalkali = round(na2Oequivavailalkali, 1)
	return roundna2Oequivavailalkali