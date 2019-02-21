# Author(s) Jeanette Gowen
# Date 5/31/2018
# Title FillEntityAttributeChemCE
# Module specific to Chem Analysis for CE (used in onsave)
# Code version 1.00
# Type (Python Custom Module)

def fillEntity(Entity, LOImysortedList, chemanalmysortedList, sulfideanalmysortedList):
    for index in range(0, len(LOImysortedList)):
        if LOImysortedList[index].Order == 1:
            Entity.LOITareWeight = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 2:
            Entity.LOISampleWeight = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 3:
            Entity.LOIIgnitionWt550 = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 4:
            Entity.LOIIgnitionWt950 = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 6:
            Entity.InsolubleResSample = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 7:
            Entity.InsolubleResTare = LOImysortedList[index].RowValue
        elif LOImysortedList[index].Order == 8:
            Entity.InsolubleResIgnition = LOImysortedList[index].RowValue

    for index in range(0, len(chemanalmysortedList)):
        if chemanalmysortedList[index].Order == 12:
            Entity.Ca3Al = chemanalmysortedList[index].RowValue

    for index in range(0, len(sulfideanalmysortedList)):
        if sulfideanalmysortedList[index].Order == 1:
            Entity.SO3SampleWt = sulfideanalmysortedList[index].RowValue
        elif sulfideanalmysortedList[index].Order == 2:
            Entity.SO3TareWt = sulfideanalmysortedList[index].RowValue
        elif sulfideanalmysortedList[index].Order == 3:
            Entity.SO3WtPlusTare = sulfideanalmysortedList[index].RowValue
        elif sulfideanalmysortedList[index].Order == 4:
            Entity.SulfideSampleWt = sulfideanalmysortedList[index].RowValue
        elif sulfideanalmysortedList[index].Order == 5:
            Entity.SulfideVolKlO3 = sulfideanalmysortedList[index].RowValue

