# Author(s) Jeanette Gowen
# Date 11/25/2018
# Title SpecificationValueNoRound
# used to get specification value
# specvaluetype -- ie MaxLimit, TargetValue
# Code version 1.00
# Type (Python Custom Module)


import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import RefSpecificationConditionField

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
                specval = getattr(testConditionField, specvaluetype)
    return specval

