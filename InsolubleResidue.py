# Author(s) Jeanette Gowen
# Date 5/29/2018
# Title PercentCO2
# Used to calculate Insoluble Residue
# Code version 1.00
# Type (Python Custom Module)

def calcInsolubleResidue( insolubleResSample, insolubleResTar, insolubleResIgnition ):
	roundperInsolubleResidue = None
	if insolubleResSample and insolubleResTar and insolubleResIgnition:
		percentInsolubleResidue = ((insolubleResIgnition - insolubleResTar)/(insolubleResSample))*100
		roundperInsolubleResidue = round(percentInsolubleResidue, 2)
	return roundperInsolubleResidue