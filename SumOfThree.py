# Author(s) Michael Elasky
# Date 4/27/2018
# Title SumOfThree
# Used to calculate SiO2 % + Al2O3 % + Fe2O3 %
# Code version 1.00
# Type (Python Custom Module)

def calcsumofThree(SiO2per, Al2O3per, Fe2O3per):
	roundsumofThree = None
	if SiO2per and Al2O3per and Fe2O3per:
		sumofThree = SiO2per + Al2O3per + Fe2O3per
		roundsumofThree = round(sumofThree, 1)
	return roundsumofThree