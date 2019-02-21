# Author(s) Michael Elasky
# Date 4/27/2018
# Title GetInstanceId
# Used to get instance id from MaterialTest
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import MaterialTest, SampleRecordTest, AgencyEntityInstance

def getMaterialTestId(Repo, testMethod):
	materialTestId = None
	materialTest = Repo.Retrieve[MaterialTest]({'Method': testMethod})
	if materialTest:
		materialTestId = materialTest.Id
	return materialTestId

def getAgencyEntityInstanceId(Repo, testMethod, sampleRecordId):
	materialTestId = getMaterialTestId(Repo, testMethod)
	instanceId = None
	validSRTs = []
	validSRTs = Repo.List[SampleRecordTest]({'SampleRecordId': sampleRecordId, 'MaterialTestId': materialTestId})
	if len(validSRTs) > 0:
		validSRTs = sorted(validSRTs, key=lambda x: x.TestRuns)
		agencyEntityInstances = Repo.List[AgencyEntityInstance]({'BaseModelParentId': validSRTs[0].Id })
		if agencyEntityInstances:
			instanceId = agencyEntityInstances[0].Id

	return instanceId
	
	
