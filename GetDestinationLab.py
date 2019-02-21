# Author(s) Michael Elasky
# Date 4/27/2018
# Title GetDestinationLab
# Used to get the destination lab
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import LabUnit, Lab

def getdestinationlab(Repo,ParentEntity,labunitid):
	labname = None
	labunits = Repo.List[LabUnit]({'Id':labunitid})
	for labunit in labunits:
		lab = labunit.LabId
	labs = Repo.List[Lab]({'Id':lab})
	for lab in labs:
		labname = lab.Name
	return labname