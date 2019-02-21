#import clr
#clr.AddReference(r'Repository.Models')
#from Repository.Models import *

def init(repo, parentEntity, entity=None, agencyEntityInstancesData=None):
	global Repo
	global ParentEntity

	Repo = repo
	ParentEntity = parentEntity

	if agencyEntityInstancesData is not None:
		global AgencyEntityInstancesData
		AgencyEntityInstancesData = agencyEntityInstancesData
		
	if entity is not None:
		global Entity
		Entity = entity


