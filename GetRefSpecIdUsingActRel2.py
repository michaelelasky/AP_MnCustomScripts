# Author(s) Michael Elasky
# Date 4/27/2018
# Title GetRefSpecidUsingActRel
# Used to get the actionrelation id
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import *

def getspecid(Repo,ParentEntity):
	samplerefspec = Repo.Retrieve[SampleTestRefSpecification]({'SampleRecordTestId': ParentEntity.Id, 'UseForTest': True})
	refspeccond = None
	samplerecordid = Repo.Retrieve[SampleRecord]({'Id':ParentEntity.SampleRecordId})
	materailid = Repo.Retrieve[Material]({'Id':samplerecordid.MaterialId})
	actionrelationshipdescription = '%s Specification' %materailid.Name
	actionrelation = Repo.Retrieve[ActionRelationship]({'Description': actionrelationshipdescription})
	refspecifications = Repo.List[RefSpecification]({'ActionRelationshipId' :actionrelation.Id,'Status' : 'ACTIVE'}) 
	if refspecifications is not None:
		if len(refspecifications) == 1:
			for refspecification in refspecifications:
				refspecificationname = refspecification.Id	
		elif len(refspecifications) > 1:
			for refspecification in refspecifications:
				refspeccondname = Repo.Retrieve[RefSpecificationCondition]({'RefSpecificationId' : refspecification.Id})
				refspecificationname = refspecification.Id
				
		actionrelationId = actionrelation.Id
	return actionrelationId