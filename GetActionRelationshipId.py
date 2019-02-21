# Author(s) Michael Elasky
# Date 11/28/2018
# Title ActionRelationshipId
# used get an actionrelationshipid from the material id and refspecification
# Code version 1.00
# Type (Python Custom Module)

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import RefSpecification, ActionRelationship, Material,SampleTestRefSpecification,SampleRecord

def getactionrelationshipId(Repo,ParentEntity):
	samplerefspec = Repo.Retrieve[SampleTestRefSpecification]({'SampleRecordTestId': ParentEntity.Id, 'UseForTest': True})
	refspeccond = None
	actionrelationshipId = None
	samplerecordid = Repo.Retrieve[SampleRecord]({'Id':ParentEntity.SampleRecordId})
	materailid = Repo.Retrieve[Material]({'Id':samplerecordid.MaterialId})
	actionrelationshipdescription = '%s Specification' %materailid.Name
	actionrelation = Repo.Retrieve[ActionRelationship]({'Description': actionrelationshipdescription})
	refspecifications = Repo.List[RefSpecification]({'ActionRelationshipId' :actionrelation.Id,'Status' : 'ACTIVE'}) 
	if refspecifications is not None:
		if len(refspecifications) >= 1:
			for refspecification in refspecifications:
				actionrelationshipId = refspecification.ActionRelationshipId 
		return actionrelationshipId
	
