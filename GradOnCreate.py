# Author(s) Mike Elasky
# Date 01/13/2018
# Title GradOnCreate
# used for Gradation view creation
# Code version 2.00
# Type (Python Custom Module)



import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import AgencyEntityInstance, AgencyEntity, MaterialTest, RefCodeTableValue
from GetRefSpecValue import *
import awp


def main(Repo, ParentEntity,t27detailname, t27listname, t27ratiolistname,t27matchpanlistname,sievecodetablename,ratocodetablename,matchpancodetablename):
	instdata = {}
	t27detailinst = create_t27detailinst_instance(Repo,ParentEntity,t27detailname)
	
	
	global refspeccond
	refspeccond = get_spec_id(Repo,ParentEntity)
	#global refspeccondfield
	#refspeccondfield = Repo.Retrieve[RefSpecificationConditionField]({'RefSpecificationConditionId': refspeccond.Id})
	#labunit = Repo.Retrieve[LabUnit]({'Id': ParentEntity.LabUnitId})
	#if 'Construction' in labunit:
		#sievecodetable = sievecodetablename
	#else:
		#sievecodetable = sievecodetablenames
	submit_entity_instdata_for_save(t27detailinst, instdata)
	create_sieve_instances(Repo,ParentEntity,t27detailinst, t27listname, sievecodetablename) #submit_entity_instdata_for_save,instance, datadict)
	create_sieve_instances(Repo,ParentEntity,t27detailinst, t27ratiolistname, ratocodetablename) #submit_entity_instdata_for_save,instance, datadict)
	create_sieve_instances(Repo,ParentEntity,t27detailinst, t27matchpanlistname, matchpancodetablename)


	
	
def create_t27detailinst_instance(Repo,ParentEntity,t27detailname):
	t27detailinst = Repo.RetrieveByName[AgencyEntity](t27detailname)

	if t27detailinst is None:
		raise Exception('{0} No Agency Entity'.format(t27detailname))
	return create_agency_entity_instance(t27detailinst.Id, ParentEntity.Id)

    
def create_sieve_instances(Repo,ParentEntity,t27detailinst, t27listname, codetablename):
	aesieve = Repo.RetrieveByName[AgencyEntity](t27listname)
	
	if aesieve is None:
		raise Exception('{0} Age'.format(t27listname))
	
	testmethod = Repo.Retrieve[MaterialTest]({'Id' : ParentEntity.MaterialTestId})
	method = testmethod.Method
	order = 0
	orderratio = 1
	ordermatch = 1
	numberfour = False
	table = set()
	GradationCodeTableValueFilter = { 'RefCodeTable.Name': codetablename } #'Grad Sieves' }
	sieves = sorted(Repo.List[RefCodeTableValue](GradationCodeTableValueFilter), key=lambda x: x.Name)
	
	for sieve in sieves:
		if codetablename == 'Grad Sieves':
			s,a = sieve.Name.split()
			if s in method:
				items=sieve.Description.split(';')
				x = {}
				for item in items:
					key,value = item.split('=')
					x[key] = value.split(',')
				for key in sorted(x.iterkeys()):
					if x[key][0] not in table:
						table.add(x[key][0])
						if len(x[key])>1:
							coarseflag = 1
						else:
							coarseflag = 0
							
						create_t27list_record(Repo,ParentEntity,aesieve.Id, t27detailinst, x[key][0], order, coarseflag)
						
						order += 1
						
		elif codetablename == 'Grad Ratio':
			value = sieve.Description
			create_mylist_record(Repo,ParentEntity,aesieve.Id, t27detailinst, value, orderratio)
			orderratio += 1
			
		elif codetablename == 'Grad Match Pan':
			value = sieve.Description
			create_mylistmatch_record(Repo,ParentEntity,aesieve.Id, t27detailinst, value, ordermatch)
			ordermatch += 1

					
					
def create_t27list_record(Repo,ParentEntity,aesieveId, t27detailinst, value, order, IsCoarseFlag):
	sinst = create_agency_entity_instance(aesieveId)
	sinst.AgencyEntityInstanceParent = t27detailinst
	minlimit,maxlimit = get_spec_value(Repo,ParentEntity,value,None,refspeccond)
	sdata = {}
	sdata['Order'] = order
	sdata['SieveSize'] = value
	sdata['MinPctPassing'] = minlimit
	sdata['MaxPctPassing'] = maxlimit
	sdata['IsCoarseFlag'] = IsCoarseFlag
    
	submit_entity_instdata_for_save(sinst, sdata)
	
def create_t27detail_record(Repo,ParentEntity,aesieveId, t27detailinst, refspecconditionName):
	dinst = create_agency_entity_instance(t27detailinst)
	#dinst.AgencyEntityInstanceParent = t27detailinst
	ddata = {}
	
	ddata['RefSpecConditionName'] = refspecconditionName
    
	submit_entity_instdata_for_save(sinst, ddata)
	
   
def create_mylist_record(Repo,ParentEntity,aelistId, t27detailinst, value, orderratio):
	rowinstance = create_agency_entity_instance(aelistId)
	rowinstance.AgencyEntityInstanceParent = t27detailinst
	minlimit,maxlimit = get_spec_value(Repo,ParentEntity,value,None,refspeccond)
	rowsinstdata = {}
	rowsinstdata['Order'] = orderratio
	rowsinstdata['Label'] = value
	rowsinstdata['SpecMin'] = minlimit
	rowsinstdata['SpecMax'] = maxlimit
    
	submit_entity_instdata_for_save(rowinstance, rowsinstdata)
	

	
def create_mylistmatch_record(Repo,ParentEntity,aelistId, t27detailinst, value, ordermatch):
	rowsinst = create_agency_entity_instance(aelistId)
	rowsinst.AgencyEntityInstanceParent = t27detailinst
	rowsdata = {}
	rowsdata['Order'] = ordermatch
	rowsdata['FieldLabel'] = value
    
	submit_entity_instdata_for_save(rowsinst, rowsdata)
    

def create_agency_entity_instance(agencyentityid, baseModelParentId=None):
	instance = AgencyEntityInstance()
	instance.AgencyEntityId = agencyentityid
	instance.BaseModelParentId = baseModelParentId
	return instance


def submit_entity_instdata_for_save(instance, datadict):
		awp.AgencyEntityInstancesData[instance] = datadict