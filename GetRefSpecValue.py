# Author(s) Michael Elasky
# Date 4/27/2018
# Title GetRefSpecValue
# Used to get the RefSpecifications
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import SampleRecord, Material, ActionRelationship, RefSpecification, RefSpecificationCondition, RefSpecificationConditionField

def get_spec_id(Repo,ParentEntity):
	refspeccond = None
	samplerecordid = Repo.Retrieve[SampleRecord]({'Id':ParentEntity.SampleRecordId})
	materailid = Repo.Retrieve[Material]({'Id':samplerecordid.MaterialId})
	actionrelationshipdescription = '%s Specification' %materailid.Name
	actionrelation = Repo.Retrieve[ActionRelationship]({'Description': actionrelationshipdescription})
	refspecifications = Repo.List[RefSpecification]({'ActionRelationshipId' :actionrelation.Id,'Status' : 'ACTIVE'})
	if refspecifications is not None:
		if len(refspecifications) == 1:
			for refspecification in refspecifications:
				refspeccond = Repo.List[RefSpecificationCondition]({'RefSpecificationId' : refspecification.Id})
		elif len(refspecifications) > 1:
			for refspecification in refspecifications:
				refspeccond = Repo.List[RefSpecificationCondition]({'RefSpecificationId' : refspecification.Id})
				if refspecification.Name == '2018':
					refspeccond = refspeccond			
	return refspeccond
				
def get_spec_value(Repo,ParentEntity, value,refspec = None,refspeccond = None):
	if refspec is not None:
		refspecconditionID = refspec
	elif ParentEntity is not None and refspeccond is not None:
		for r in refspeccond:
			refspecconditionID = r.Id
	else:
		return
	name = None
	maxlimit = None
	minlimit = None
	targetvalue = None
	negativetargetdeviation = None
	positivetargetdeviation = None
	val = value.split('(')
	for v in val:
		v = v.strip()
		refspeccondfield = Repo.Retrieve[RefSpecificationConditionField]({'RefSpecificationConditionId': refspecconditionID, 'ConditionFieldType': 'Numeric w/ Min/Max', 'Name': v})
		if refspeccondfield is not None:
			minlimit = refspeccondfield.MinLimit
			maxlimit = refspeccondfield.MaxLimit
		return minlimit,maxlimit
		refspeccondfield = Repo.Retrieve[RefSpecificationConditionField]({'RefSpecificationConditionId': refspecconditionID, 'ConditionFieldType': 'Numeric w/ Range', 'Name': v})
		if refspeccondfield is not None:
			targetvalue = refspeccondfield.TargetValue
			negativetargetdeviation = refspeccondfield.NegativeTargetDeviation
			positivetargetdeviation = refspeccondfield.PositiveTargetDeviation
		return targetvalue, negativetargetdeviation, positivetargetdeviation