# Author(s) Michael Elasky
# Date 4/27/2018
# Title GetRefSpecValue
# Used to get the RefSpecifications on save
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import RefSpecificationConditionField
		
def get_spec_value(Repo,value,refspec = None):
	if refspec is not None:
		refspecconditionID = refspec
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
			minlimit = str(refspeccondfield.MinLimit)
			maxlimit = str(refspeccondfield.MaxLimit)
		return minlimit,maxlimit
		refspeccondfield = Repo.Retrieve[RefSpecificationConditionField]({'RefSpecificationConditionId': refspecconditionID, 'ConditionFieldType': 'Numeric w/ Range', 'Name': v})
		if refspeccondfield is not None:
			targetvalue = refspeccondfield.TargetValue
			negativetargetdeviation = refspeccondfield.NegativeTargetDeviation
			positivetargetdeviation = refspeccondfield.PositiveTargetDeviation
		return targetvalue, negativetargetdeviation, positivetargetdeviation