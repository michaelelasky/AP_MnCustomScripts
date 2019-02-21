# Author(s) Mike Elasky
# Date 7/30/2018
# Title RoundTenScientific
# Used to used round to the nearest 10th place
# Code version 1.00
# Type (Python Custom Module)

def roundTenScientific(num):
	from ScientificRounding import scientific_rounding
	if not num:
		return
	n = scientific_rounding(num, precision = 0)
	rem = int(n % 10)
	divisor = int(n / 10)
	if rem <= 4: #round down
		n = int(n / 10) * 10
	elif rem == 5 and divisor % 2 == 0: #round down to nearest even
		n = int(n / 10) * 10
	else:
		n = int((n + 10) / 10) * 10
	return float(n)