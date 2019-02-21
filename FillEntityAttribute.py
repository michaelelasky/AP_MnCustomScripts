# Author(s) Michael Elasky
# Date 5/16/2018
# Title FillEntityAttribute
# Module specific to FA Chem Analysis Plant(used in onsave)
# Code version 1.00
# Type (Python Custom Module)

def fillEntity(Entity,LOImysortedList, chemanalmysortedList, availalkmysortedList, plantcompmysortedList):	
	for index in range(0,len(LOImysortedList)):
		if LOImysortedList[index].Order == 2:
			Entity.LOITWt = LOImysortedList[index].RowValue
		elif LOImysortedList[index].Order == 3:
			Entity.LOISpWt = LOImysortedList[index].RowValue
		elif LOImysortedList[index].Order == 4:
			Entity.LOIIgWt110 = LOImysortedList[index].RowValue
		elif LOImysortedList[index].Order == 5:
			Entity.LOIIgWt750 = LOImysortedList[index].RowValue
		
	for index in range(0,len(chemanalmysortedList)):
		if chemanalmysortedList[index].Order == 2:
			Entity.SiO2P = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 3:
			Entity.Al2O3P = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 4:
			Entity.Fe2O3P = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 5:
			Entity.CaOP = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 6:
			Entity.PercentMgO = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 7:
			Entity.PercentSO3 = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 8:
			Entity.Na2OP = chemanalmysortedList[index].RowValue
		elif chemanalmysortedList[index].Order == 9:
			Entity.K2OP = chemanalmysortedList[index].RowValue
			
	for index in range(0,len(availalkmysortedList)):
		if availalkmysortedList[index].Order == 1:
			Entity.AvNa2OP = availalkmysortedList[index].RowValue
		elif availalkmysortedList[index].Order == 2:
			Entity.AvK2OP = availalkmysortedList[index].RowValue
			
	for index in range(0,len(plantcompmysortedList)):
		if plantcompmysortedList[index].Order == 1:
			Entity.PercentLOIComp = plantcompmysortedList[index].RowValue
		elif plantcompmysortedList[index].Order == 2:
			Entity.PercentMoistureComp = plantcompmysortedList[index].RowValue
		elif plantcompmysortedList[index].Order == 6:
			Entity.SumOfThreeComp = plantcompmysortedList[index].RowValue
		elif plantcompmysortedList[index].Order == 7:
			Entity.PercentCaOComp = plantcompmysortedList[index].RowValue
		elif plantcompmysortedList[index].Order == 9:
			Entity.PercentSO3Comp = plantcompmysortedList[index].RowValue