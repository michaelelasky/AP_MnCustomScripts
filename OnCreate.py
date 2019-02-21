# Author(s) Mike Elasky
# Date 01/13/2018
# Title OnCreate
# used to enable autocomplete fields to get values without entering data into another entity attribute field
# Code version 3.00
# Type (Python Custom Module)


import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import AgencyEntity, AgencyEntityInstance
import awp

def main(Repo, ParentEntity, mydetailname):
    instdata = {}
    mydetailinst = create_mydetailinst_instance(Repo,ParentEntity,mydetailname)
    submit_entity_instdata_for_save(mydetailinst, instdata)


def create_mydetailinst_instance(Repo,ParentEntity,mydetailname):
    mydetailinst = Repo.RetrieveByName[AgencyEntity](mydetailname)
    if mydetailinst is None:
        raise Exception('{0} Agency Entity is not present'.format(mydetailname))
    return create_agency_entity_instance(mydetailinst.Id, ParentEntity.Id)


def create_agency_entity_instance(agencyentityid, baseModelParentId=None):
    instance = AgencyEntityInstance()
    instance.AgencyEntityId = agencyentityid
    instance.BaseModelParentId = baseModelParentId
    return instance


def submit_entity_instdata_for_save(instance, datadict):
    awp.AgencyEntityInstancesData[instance] = datadict