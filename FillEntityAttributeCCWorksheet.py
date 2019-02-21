# Author(s) Jeanette Gowen
# Date 8/22/2018
# Title FillEntityAttributeCCWorksheet
# Module specific to CC Worksheet (used in onsave)
# Code version 1.00
# Type (Python Custom Module)

def fillEntity(Entity, d0List, d1List, d3List):

    Entity.Mold1 = None
    Entity.Mold2 = None
    Entity.Mold3 = None
    Entity.Time1 = None
    Entity.Time2 = None
    Entity.Time3 = None
    Entity.SealWt1 = None
    Entity.SealWt2 = None
    Entity.SealWt3 = None
    Entity.PanWeight1 = None
    Entity.PanWeight2 = None
    Entity.PanWeight3 = None
    Entity.CCPanWt1 = None
    Entity.CCPanWt2 = None
    Entity.CCPanWt3 = None
    Entity.FinalWt1 = None
    Entity.FinalWt2 = None
    Entity.FinalWt3 = None
    Entity.WaterLoss24Hr1 = None
    Entity.WaterLoss24Hr2 = None
    Entity.WaterLoss24Hr3 = None
    Entity.WaterLoss72Hr1 = None
    Entity.WaterLoss72Hr2 = None
    Entity.WaterLoss72Hr3 = None

    for index in range(0, len(d0List)):
        if d0List[index].Order == 1:
            Entity.Mold1 = d0List[index].Mold
            Entity.Time1 = d0List[index].Time
            Entity.SealWt1 = d0List[index].SealWt
            Entity.PanWeight1 = d0List[index].PanWeight
            Entity.CCPanWt1 = d0List[index].CCPanWt
            Entity.FinalWt1 = d0List[index].FinalWt
        elif d0List[index].Order == 2:
            Entity.Mold2 = d0List[index].Mold
            Entity.Time2 = d0List[index].Time
            Entity.SealWt2 = d0List[index].SealWt
            Entity.PanWeight2 = d0List[index].PanWeight
            Entity.CCPanWt2 = d0List[index].CCPanWt
            Entity.FinalWt2 = d0List[index].FinalWt
        elif d0List[index].Order == 3:
            Entity.Mold3 = d0List[index].Mold
            Entity.Time3 = d0List[index].Time
            Entity.SealWt3 = d0List[index].SealWt
            Entity.PanWeight3 = d0List[index].PanWeight
            Entity.CCPanWt3 = d0List[index].CCPanWt
            Entity.FinalWt3 = d0List[index].FinalWt

    for index in range(0, len(d1List)):
        if d1List[index].Order == 1:
            Entity.WaterLoss24Hr1 = d1List[index].WaterLoss24Hr
        elif d1List[index].Order == 2:
            Entity.WaterLoss24Hr2 = d1List[index].WaterLoss24Hr
        elif d1List[index].Order == 3:
            Entity.WaterLoss24Hr3 = d1List[index].WaterLoss24Hr

    for index in range(0, len(d3List)):
        if d3List[index].Order == 1:
            Entity.WaterLoss72Hr1 = d3List[index].WaterLoss72Hr
        elif d3List[index].Order == 2:
            Entity.WaterLoss72Hr2 = d3List[index].WaterLoss72Hr
        elif d3List[index].Order == 3:
            Entity.WaterLoss72Hr3 = d3List[index].WaterLoss72Hr

