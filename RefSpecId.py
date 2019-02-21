# Author(s) Michael Elasky
# Date 05/24/2018
# Title RefSpecId
# used to get ref spec id
# Code version 1.00
# Type (Python Custom Module)


import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import SampleTestRefSpecification

def getrefspecificationId(Repo,Entity, ParentEntity):
	samplerefspec = Repo.Retrieve[SampleTestRefSpecification]({'SampleRecordTestId': ParentEntity.Id, 'UseForTest': True})
	if samplerefspec:
		refspecificationid = samplerefspec.RefSpecificationId
	return refspecificationid

	
