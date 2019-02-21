#specvaluetype -- ie MaxLimit, TargetValue

def specificationValue(Repo, SampleRecordTest, SampleTestRefSpecification, RefSpecification, RefSpecificationCondition, sampleRecordTestId, conditionname, fieldname=None, specvaluetype=None):
	specval = None

	parentSampleRecordTest = Repo.Retrieve[SampleRecordTest](sampleRecordTestId)
	Repo.LoadProperty(parentSampleRecordTest, "SampleTestRefSpecifications")
	markedForUse = [x for x in parentSampleRecordTest.SampleTestRefSpecifications if x.UseForTest == True]
	if len(markedForUse) > 0:
		useForTest = markedForUse[0]
		Repo.LoadProperty[SampleTestRefSpecification](useForTest, "RefSpecification")
		Repo.LoadProperty[RefSpecification](useForTest.RefSpecification, "RefSpecificationConditions")
		refspecconds = [x for x in useForTest.RefSpecification.RefSpecificationConditions if
							x.Name == conditionname]
		if len(refspecconds) > 0:
			refCondition = refspecconds[0]
			Repo.LoadProperty[RefSpecificationCondition](refCondition, "RefSpecificationFields")
			if fieldname:
				refConditionFields = [x for x in refCondition.RefSpecificationFields if x.Name == fieldname]
			else:
				refConditionFields = [x for x in refCondition.RefSpecificationFields]
			if len(refConditionFields) > 0:
				refConditionField = refConditionFields[0]
				specval = round(getattr(refConditionField, specvaluetype), 0)

	return specval