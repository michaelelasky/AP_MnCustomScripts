# Author(s) Michael Elasky
# Date 4/27/2018
# Title GradOnSave
# Used for on save
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import AgencyEntityInstance, AgencyEntity, MaterialTest, RefCodeTableValue
from SievesRatio import *
  
	
def grad(Repo,Entity,ParentEntity,t27listname):
    
	sieve200 = None
	sieve01 =  None
	sieve10 = None
	sieve40 = None
	
	entity = Repo.Retrieve[AgencyEntity]({'Name':t27listname})
	if entity:
		id = entity.Id
	mylist = Repo.ListAgencyEntityInstance({'AgencyEntityId': id, 'AgencyEntityInstanceParent.BaseModelParentId': ParentEntity.Id})
	mysortedlist = sorted(mylist, key=lambda x: x.Order)
	
	if Entity.TotalDrySampleWt > 0:
		listOfPreviousWt = []
		listOfPreviousWt.append('{0}'.format(Entity.TotalDrySampleWt))
		isprevcoarse = True
 		
		
		for index in range(1, len(mysortedlist)):
			if mysortedlist[index].IsCoarseFlag == 1 or not isprevcoarse:
				if mysortedlist[index-1].WtRetained is not None:
					wtRetained = mysortedlist[index-1].WtRetained
				else:
					wtRetained = 0
				currentPreviousWt = float(listOfPreviousWt[index-1]) - float(wtRetained)
				listOfPreviousWt.append('{0}'.format(currentPreviousWt))
			elif isprevcoarse:
				listOfPreviousWt.append('{0}'.format(Entity.WtBeforeWash))
				isprevcoarse = False
        
		Entity.ListOfWtPrevious = ','.join(listOfPreviousWt)
        
		for index in range(0,len(mysortedlist)):
			if mysortedlist[index].SieveSize == 'No. 200 (74 um)':
				sieve200 = mysortedlist[index].PctPassing
			elif mysortedlist[index].SieveSize == '1 in. (25 mm)':
				sieve01 = mysortedlist[index].PctPassing
			elif mysortedlist[index].SieveSize == 'No. 40 (420 um)':
				sieve40 = mysortedlist[index].PctPassing
			elif mysortedlist[index].SieveSize == 'No. 10 (2 mm)':
				sieve10 = mysortedlist[index].PctPassing
    
	if sieve200 is not None and sieve01 is not None:
		Entity.Num200_1inchRatio = sievesRatio(sieve200,sieve01)
	if sieve200 is not None and sieve10 is not None:
		Entity.Num200_Num10Ratio = sievesRatio(sieve200,sieve10)
	if sieve40 is not None and sieve10 is not None:
		Entity.Num40_Num10Ratio = sievesRatio(sieve40,sieve10)