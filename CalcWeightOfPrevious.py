# Author(s) Michael Elasky
# Date 4/27/2018
# Title CalcWeightOfPrevious
# Used to calculate weight of previous sieve
# Code version 1.00
# Type (Python Custom Module

def calcweightofPrevious(Repo,Entity, ParentEntity,listofwtprevious = None, order = None):
	wtprevious = None
	listofwtprev = None
	if ParentEntity is not None and listofwtprevious is not None and len(listofwtprevious) > 0:
		listofwtprev = listofwtprevious.split(',')
		if listofwtprev is not None:
			if len(listofwtprev) >= order:
				strorder= '{0}'.format(order)
				index = int(strorder.split('.')[0])
				previouspassingwt = float(listofwtprev[index])
				wtprevious = round(previouspassingwt, 2)
	return wtprevious