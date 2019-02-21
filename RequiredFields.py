# Author(s) Jeanette Gowen, Mike Elasky
# Date 12/6/2018
# Title RequiredFields
# Used to verify the Tester field have entries
# Code version 2.00
# Type (Python Custom Module)

def verifyrequiredfields(tester):
	error = None
	if tester is None:
		error = 'Tester is Required'

	return error