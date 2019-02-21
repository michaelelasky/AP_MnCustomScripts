# Author(s) Michael Elasky
# Date 4/27/2018
# Title CalcTotalSievesWt
# Used to calculate total weight of sieves
# Code version 1.00
# Type (Python Custom Module

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import  AgencyEntity

def calctotalsieveswt(Repo,Entity,ParentEntity,sieveswt,lossonwash):
	sieveswtlist = Repo.RetrieveByName[AgencyEntity](sieveswt)
	instancesieveslist = Repo.ListAgencyEntityInstance({'AgencyEntityId': sieveswtlist.Id, 'AgencyEntityInstanceParent.BaseModelParentId': ParentEntity.Id})
	sortedinstancesieveslist = sorted(instancesieveslist, key=lambda x: x.Order)
	
	totalcoarsesievewt = 0
	totalfinesievewt = 0
	
	for index in range(1, len(sortedinstancesieveslist)):
		if sortedinstancesieveslist[index].IsCoarseFlag == 1 and sortedinstancesieveslist[index].WtRetained:
			totalcoarsesievewt = totalcoarsesievewt + float(sortedinstancesieveslist[index].WtRetained)
		elif sortedinstancesieveslist[index].IsCoarseFlag != 1 and sortedinstancesieveslist[index].WtRetained and lossonwash:
			totalfinesievewt = totalfinesievewt + float(sortedinstancesieveslist[index].WtRetained) + lossonwash
	return totalcoarsesievewt,totalfinesievewt