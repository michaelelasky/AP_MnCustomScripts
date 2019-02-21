# Author(s) Jeanette Gowen
# Date 8/2/2018
# Title RetrieveCalibrationFactor
# Used to retrieve the first Test Equipment for the specified Current Assignment sorted by Serial Number
# Code version 1.00
# Type (Python Custom Module)

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import TestEquipment

# calibrationFactor is retrieved from Test Equipment using Id stored in zievenum
def retrieveCalibrationFactor(Repo, sievenum):

    calibrationFactor = None
    if sievenum is not None:
        testEquipment = Repo.Retrieve[TestEquipment]({'Id': sievenum})
        if testEquipment is not None:
            calibrationFactor = round(testEquipment.CALIBRATIONFACTOR,2)

    return calibrationFactor

