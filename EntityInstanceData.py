# Author(s) Michael Elasky
# Date 05/24/2018
# Title EntityInstanceData
# used to get data from another Entity Instance with conditions
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

def getAgencyEntityInstanceId(Repo,agentityid,date,datevalue,breakday,breakdayyvalue):
	id1 = None
	id2 = None
	instanceid = None
	agentityinstances = Repo.List[AgencyEntityInstance]({'AgencyEntityId':agentityid})
	if len(agentityinstances) > 0:
		for agentityinstance in agentityinstances:
			agentityinstanceid = getattr(agentityinstance,'Id')
			agentityinstdata = Repo.List[AgencyEntityInstanceData]({'AgencyEntityInstanceId':agentityinstanceid, })
			if len(agentityinstdata) > 0:
				for d in agentityinstdata:
					k = getattr(d,'Key')
					v = getattr(d,'Value')
					if k == date and  v == datevalue:
						id1 =  getattr(d,'AgencyEntityInstanceId')
					if k == breakday and  v == breakdayyvalue:
						id2 =  getattr(d,'AgencyEntityInstanceId')
					if id1 and id2:
						if id1 == id2:
							instanceid = id1
	return instanceid
						
def getAgencyEntityInstanceData(Repo,entityname,key,date,datevalue,breakday,breakdayyvalue):
	instancedata = None
	agentityid = getAgencyEntityId(Repo,entityname)
	if agentityid:
		instanceid = getAgencyEntityInstanceId(Repo,agentityid,date,datevalue,breakday,breakdayyvalue)
		if instanceid:
			agentityinstdata = Repo.List[AgencyEntityInstanceData]({'AgencyEntityInstanceId':instanceid, })
			if len(agentityinstdata) > 0:
				for i in agentityinstdata:
					f = getattr(i,'Key')
					if f == key:
						instancedata = getattr(i,'Value')
	return instancedata

