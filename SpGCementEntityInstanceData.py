# Author(s) Jeanette Gowen, Mark Oelke
# Date 08/14/2018
# Title SpGCementEntityInstanceData
# used to get data from another Entity Instance with conditions
# example -- Entity.ReportedSpG = getAgencyEntityInstanceData(__RepoUtils,
# 'SpecGravityD001','SpG Cement',ParentEntity.SampleRecordId )
# Code version 2.00
# Type (Python Custom Module)

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import MaterialTest, SampleRecordTest, AgencyEntityInstance, AgencyEntityInstanceData

def getMaterialTestId(Repo, testMethod):
	materialTestId = None
	materialTest = Repo.Retrieve[MaterialTest]({'Method': testMethod})
	if materialTest:
		materialTestId = materialTest.Id
	return materialTestId

def getAgencyEntityInstanceId(Repo, materialTestId, sampleRecordId):
	instanceId = None
	validSRTs = []
	validSRTs = Repo.List[SampleRecordTest]({'SampleRecordId': sampleRecordId, 'MaterialTestId': materialTestId})
	if len(validSRTs) > 0:
		validSRTs = sorted(validSRTs, key=lambda x: x.TestRuns)
		agencyEntityInstances = Repo.List[AgencyEntityInstance]({'BaseModelParentId': validSRTs[0].Id })
		if agencyEntityInstances:
			instanceId = agencyEntityInstances[0].Id

	return instanceId


def getAgencyEntityInstanceData(Repo, testMethod, field1, sampleRecordId):
	instancedata = None
	materialTestId = getMaterialTestId(Repo, testMethod)

	if materialTestId:
		instanceId = getAgencyEntityInstanceId(Repo, materialTestId, sampleRecordId)
		if instanceId:
			agencyEntityinstdata = Repo.Retrieve[AgencyEntityInstanceData](
			{'AgencyEntityInstanceId': instanceId, 'Key': field1})
			if agencyEntityinstdata is not None:
				instancedata = agencyEntityinstdata.Value
				if instancedata is not None:
					instancedata = float(instancedata.replace(',', ''))
			return instancedata


