# Author(s) Mike Elasky
# Date 01/10/2019
# Title BlaineOnCreate
# used to get data from another RefSpecification Instance
# example -- main(__RepoUtils, ParentEntity,'Blaine_004')
# Code version 1.00
# Type (Python Custom Module)

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import RefSpecification, RefSpecificationCondition, RefSpecificationConditionField, AgencyEntity, AgencyField
from GetInstanceId import *
import awp

def main(Repo,ParentEntity,detailname):
	agencyFields = None
	sdata = {}
	refspecificationconditionId = Repo.Retrieve[RefSpecificationCondition]({'Name':'Factors'})
	if refspecificationconditionId is None:
		raise Exception('No C204 Calibration' )
	testConditionFields = Repo.List[RefSpecificationConditionField]({'RefSpecificationConditionId': refspecificationconditionId.Id })
	agencydetailId = Repo.Retrieve[AgencyEntity]({'Name':detailname})
	agencyFields = Repo.List[AgencyField]({'AgencyEntityId': agencydetailId.Id})
	detailinstId = create_agency_entity_instance(agencydetailId.Id, ParentEntity.Id)
	for testConditionField in testConditionFields:
		if agencyFields:
			for agencyField in agencyFields:
				if testConditionField.Name in agencyField.Name:
					if testConditionField.TargetValue is not None:
						#if targetValue:
							#raise Exception('{0} -- value'.format(agencyField.Name))
						sdata[agencyField.Name]=testConditionField.TargetValue
				else:
					sdata.update(agencyField = agencyField)
						
	submit_entity_instdata_for_save(detailinstId,sdata)
	
def create_agency_entity_instance(agencyentityid, baseModelParentId=None):
	instance = AgencyEntityInstance()
	instance.AgencyEntityId = agencyentityid
	instance.BaseModelParentId = baseModelParentId
	return instance

def submit_entity_instdata_for_save(instance, datadict):
		awp.AgencyEntityInstancesData[instance] = datadict