# Author(s) Michael Elasky
# Date 4/13/2018
# Title PercentSulfide
# Used to calculate Percent Sulfide.
# Code version 1.00
# Type (Python Custom Module)

def getPercentSulfide(SulfideVolKlO3, SulfideSampleWt):
	percSulfide = None
	if SulfideVolKlO3 and SulfideSampleWt:
		try:
			percSulfide = 0.04809 * SulfideVolKlO3 / SulfideSampleWt
		except ZeroDivisionError:
			return True
		else:
			return percSulfide