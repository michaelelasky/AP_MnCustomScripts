# Author(s) Michael Elasky
# Date 05/24/2018
# Title AutoClaveEntityInstanceData
# used to get data from another Entity Instance with conditions
# example -- Entity.AutoclaveDrop = getAgencyEntityInstanceData(__RepoUtils,
    #'AutoclaveDetail_001','AutoClDrop', 'SampleRecordId' , Entity.SampleRecordId,
	#'SampleRecordTestId' , Entity.SampleRecordTestId)
# Code version 1.00
# Type (Python Custom Module)

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import AgencyEntity, AgencyEntityInstance, AgencyEntityInstanceData

def getAgencyEntityId(Repo,entityname):
	agentityid = None
	agentity = Repo.Retrieve[AgencyEntity]({'Name': entityname })
	if agentity:
		agentityid = getattr(agentity,'Id')
	return agentityid

def getAgencyEntityInstanceId(Repo,agentityid,samplerecordId,samplerecordidValue,samplerecordtestId,samplerecordtestidValue):
	id1 = None
	id2 = None
	instanceid = None
	agentityinstances = Repo.List[AgencyEntityInstance]({'AgencyEntityId':agentityid})
	if len(agentityinstances) > 0:
		for agentityinstance in agentityinstances:
			agentityinstanceid = getattr(agentityinstance,'Id')
			agentityinstdata = Repo.List[AgencyEntityInstanceData]({'AgencyEntityInstanceId':agentityinstanceid, })
			if len(agentityinstdata) > 0:
				instanceid = None
				for d in agentityinstdata:
					instanceid = getattr(d,'AgencyEntityInstanceId')
					k = getattr(d,'Key')
					v = getattr(d,'Value')
					if k == str(samplerecordId) and  v == str(samplerecordidValue):
						id1 =  getattr(d,'AgencyEntityInstanceId')
					if k == str(samplerecordtestId) and  v == str(samplerecordtestidValue):
						id2 =  getattr(d,'AgencyEntityInstanceId')
					if id1 and id2:
						if id1 == id2:
							instanceid = id1
	return instanceid
						
def getAgencyEntityInstanceData(Repo,entityname,key,samplerecordId,samplerecordidValue,samplerecordtestId,samplerecordtestidValue):
	instancedata = None
	agentityid = getAgencyEntityId(Repo,entityname)
	if agentityid:
		instanceid = getAgencyEntityInstanceId(Repo,agentityid,samplerecordId,samplerecordidValue,samplerecordtestId,samplerecordtestidValue)
		instancedata = instanceid
		if instanceid:
			agentityinstdata = Repo.List[AgencyEntityInstanceData]({'AgencyEntityInstanceId':instanceid, })
			if len(agentityinstdata) > 0:
				for i in agentityinstdata:
					f = getattr(i,'Key')
					if f == key:
						instancedata = getattr(i,'Value')
	return instancedata

