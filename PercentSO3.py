# Author(s) Michael Elasky
# Date 4/13/2018
# Title PercentSO3
# Used to calculate Percent SO3.
# Code version 1.00
# Type (Python Custom Module)

def getPercentSO3(SO3WtPlusTareWt, SO3TareWt, SO3SampleWt):
	perSO3 = None
	if SO3WtPlusTareWt and SO3TareWt and SO3SampleWt:
		try:
			perSO3 = ((SO3WtPlusTareWt - SO3TareWt) / SO3SampleWt * 34.3)
		except ZeroDivisionError:
			return True
		else:
			return perSO3
		