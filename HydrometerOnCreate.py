# Author(s) Mike Elasky
# Date 01/13/2018
# Title GradCreate
# used for Gradation view creation
# Code version 2.00
# Type (Python Custom Module)



import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import AgencyEntity, AgencyEntityInstance
#from GetRefSpecValue import *
#from GetRefSpecificationConditionName import *
import awp


def main(Repo, ParentEntity,detailname, listname):
	instdata = {}
	detailinst = createdetailInstance(Repo,ParentEntity,detailname)

	submitentityinstdataforSave(detailinst, instdata)
	
	createhydrometerInstance(Repo,ParentEntity,detailinst, listname)


	
def createdetailInstance(Repo,ParentEntity,detailname):
	detailinst = Repo.RetrieveByName[AgencyEntity](detailname)

	if detailinst is None:
		raise Exception('{0} No Agency Entity'.format(detailname))
	return create_agency_entity_instance(detailinst.Id, ParentEntity.Id)

    
def createhydrometerInstance(Repo,ParentEntity,detailinst, listname):
	aesieve = Repo.RetrieveByName[AgencyEntity](listname)
	
	if aesieve is None:
		raise Exception('{0} Age'.format(listname))
	
	order = 0

	hydrometerlabelLists = [['Temp At 2 Min','Reading At 2 Min','Size at 2 Min','Pct Finer at 2 Min'],['Temp At 5 Min','Reading At 5 Min','Size at 5 Min',\
	'Pct Finer at 5 Min'],['Temp At 15 Min','Reading At 15 Min','Size at 15 Min','Pct Finer at 15 Min'],['Temp At 30 Min','Reading At 30 Min','Size at 30 Minutes',\
	'Pct Finer at 30 Min'],['Temp At 60 Min','Reading At 60 Min','Size at 60 Minu','Pct Finer at 60 Min'],['Temp At 250 Min','Reading At 250 Min',\
	'Size at 250 Min','Pct Finer at 250 Min'],['Temp At 24 Hrs','Reading At 24 Hrs','Size at 24 Hrs','Pct Finer at 24 Hrs']]
	

						
	for hydrometerlabelList in hydrometerlabelLists:
			createlistRecord(Repo,ParentEntity,aesieve.Id, detailinst, hydrometerlabelList, order)
			order += 1
					
def createlistRecord(Repo,ParentEntity,aesieveId, detailinst, value, order):
	sinst = create_agency_entity_instance(aesieveId)
	sinst.AgencyEntityInstanceParent = detailinst
	
	sdata = {}
	
	sdata['TempLabel'] = value[0]
	sdata['TempValue'] = None
	sdata['ReadingLabel'] = value[1]
	sdata['ReadingValue'] = None
	sdata['SizeLabel'] = value[2]
	sdata['SizeValueCalc'] = None
	sdata['FinerLabel'] = value[3]
	sdata['FinerValueCalc'] = None
	sdata['Order'] = order
    
	#remark = sdata
	#if remark:
		#raise Exception(str(remark))
		
	submitentityinstdataforSave(sinst, sdata)
	 

def create_agency_entity_instance(agencyentityid, baseModelParentId=None):
	instance = AgencyEntityInstance()
	instance.AgencyEntityId = agencyentityid
	instance.BaseModelParentId = baseModelParentId
	return instance


def submitentityinstdataforSave(instance, datadict):
		awp.AgencyEntityInstancesData[instance] = datadict