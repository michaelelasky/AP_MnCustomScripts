# Author(s) Mike Elasky
# Date 12/24/2018
# Title CalcGradMatchPanMaterial
# used to calculate material of the match pan
# Code version 1.00
# Type (Python Custom Module)

def calcgradmatchpanMaterial(panmaterialwt=None,panwt=None):
	materialwt=None
	if panmaterialwt and panwt:
		materialwt = panmaterialwt - panwt
	return materialwt