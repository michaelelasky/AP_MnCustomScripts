# Author(s) Jeanette Gowen
# Date 7/30/2018
# Title RetrieveFirstTestEquipment
# Used to retrieve the first Test Equipment for the specified Current Assignment sorted by Serial Number
# Code version 1.00
# Type (Python Custom Module)

import clr
clr.AddReference(r'Repository.Models')
from Repository.Models import TestEquipment

def retrieveFirstSieve(Repo, currentassignment):
    # default the sieve to the first test equipment record for the current assignment
    sieveNum = None
    testEquipments = Repo.List[TestEquipment]({'CurrentAssignment': currentassignment})
    if testEquipments is not None:
        sortedlist = sorted(testEquipments, key=lambda x: x.SerialNumber)
        if sortedlist is not None:
            testEquipment = sortedlist[0]
            if testEquipment is not None:
                sieveNum = testEquipment.Id

    return sieveNum
