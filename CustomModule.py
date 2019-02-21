import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import *

import awp

def submit_entity_instdata_for_save(instance, datadict): 
	awp.AgencyEntityInstancesData[instance]=datadict
	
	
	###

