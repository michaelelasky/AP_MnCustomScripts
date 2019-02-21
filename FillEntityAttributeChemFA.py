# Author(s) Jeanette Gowen
# Date 11/15/2018
# Title FillEntityAttributeChemFA
# Module specific to Chem Analysis for FA (used in onsave)
# Code version 2.00
# Type (Python Custom Module)

def fillEntity(Entity, LOImysortedList, chemanalmysortedList, availalkalimysortedList):
    for index in range(0, len(LOImysortedList)):
        if LOImysortedList[index].Order == 1:
            Entity.LOITWt = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 2:
            Entity.LOISpWt = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 3:
            Entity.LOIIgWt110 = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 4:
            Entity.LOIIgWt750 = LOImysortedList[index].RowValue

    for index in range(0, len(chemanalmysortedList)):
        if chemanalmysortedList[index].Order == 1:
            Entity.SiO2P = chemanalmysortedList[index].RowValue
        elif chemanalmysortedList[index].Order == 2:
            Entity.Al2O3P = chemanalmysortedList[index].RowValue
        elif chemanalmysortedList[index].Order == 3:
            Entity.Fe2O3P = chemanalmysortedList[index].RowValue
        elif chemanalmysortedList[index].Order == 4:
            Entity.CaOP = chemanalmysortedList[index].RowValue
        elif chemanalmysortedList[index].Order == 6:
            Entity.SO3P = chemanalmysortedList[index].RowValue
        elif chemanalmysortedList[index].Order == 7:
            Entity.Na2OP = chemanalmysortedList[index].RowValue
        elif chemanalmysortedList[index].Order == 8:
            Entity.K2OP = chemanalmysortedList[index].RowValue

    for index in range(0, len(availalkalimysortedList)):
        if availalkalimysortedList[index].Order == 1:
            Entity.AvNa2OP = availalkalimysortedList[index].RowValue
        elif availalkalimysortedList[index].Order == 2:
            Entity.AvK2OP = availalkalimysortedList[index].RowValue


