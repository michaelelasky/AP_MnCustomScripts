# Author(s) Michael Elasky; Jeanette Gowen
# Date 05/16/2018
# Title SpecificationValueITI_20180516
# used to get specification value
# specvaluetype -- ie MaxLimit, TargetValue
# Code version ?.??
# Type (Python Custom Module)


import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import *

def getspecificationValue(Repo, refSpecificationConditionId=None, fieldname=None, specvaluetype=None):
    specval = None
    if refSpecificationConditionId and specvaluetype:
        if fieldname:
            testConditionFields = Repo.List[RefSpecificationConditionField](
                {'RefSpecificationConditionId': refSpecificationConditionId, 'Name': fieldname})
        else:
            testConditionFields = Repo.List[RefSpecificationConditionField](
                {'RefSpecificationConditionId': refSpecificationConditionId})
        if len(testConditionFields) > 0:
            testConditionField = testConditionFields[0]
            if testConditionField:
                #specval = round(getattr(testConditionField, specvaluetype), 0)
				specval = getattr(testConditionField, specvaluetype)
				if specval is not None:
					specval = round(specval,0)
    return specval

