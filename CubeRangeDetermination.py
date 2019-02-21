# Saved as C:\AP_MnCustomScripts\CubeRangeDetermination.py
# The following code goes in the Agency Entity compStrengthDayi Field calculation.
# cube1Dayi, cube2Dayi, and cube3Dayi are input arguments.   compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi are returned
#    and should be used to set the appropriate Agency Entity Fields.
# 'Red' if (Entity.Std3RemovedDayi in ['on', 'True']) else 'Black'
# Code to include in Agency Entity Field for compStrengthDayi calculation:

#import sys
#sys.path.append('C:\AP_MnCustomScripts')  # path where ScientificRounding.py and CubeRangeDetermination,py exist on the application server
#import CubeRangeDetermination
#compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi  = CubeRangeDetermination.CalcComprensiveStrength(Entity.<cube1Dayi field name>, Entity.<cube2Dayi field name>, Entity.<cube3Dayi field name>)
#Use the return values to set the appropriate Agency Entity Fields

import ScientificRounding

def CalcComprensiveStrength(cube1Dayi,cube2Dayi,cube3Dayi):

    #Set in case row is recalculated
	cube1RemovedDayi = False
	cube2RemovedDayi = False
	cube3RemovedDayi = False
	commentsDayi = None


	#if (CheckValue(cube1Dayi) == 0 and CheckValue(cube2Dayi) == 0 and CheckValue(cube3Dayi) == 0): #All three cubes are zero
	#	compStrengthDayi = None
	#	cube1RemovedDayi = True
	#	cube2RemovedDayi = True #MRE Added
	#	cube3RemovedDayi = True #MRE Added
	#	commentsDayi = "Retest required for this sample"
	#	return compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi

	cube1 = Cube(cube1Dayi)
	cube2 = Cube(cube2Dayi)
	cube3 = Cube(cube3Dayi)

	compStrengthDayi = (cube1.PSI + cube2.PSI + cube3.PSI) / 3.0
	compStrengthDayi = ScientificRounding.scientific_rounding(compStrengthDayi, 0)
	deviation = compStrengthDayi * .087
	minCube3 = compStrengthDayi - deviation
	maxCube3 = compStrengthDayi + deviation
	
	if cube1Dayi == 1 and cube2Dayi == 2 and cube3Dayi == 3:
		commentsDayi = 'Bingo...You found this!!!'
		return compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi


	if compStrengthDayi == 0: #All three cubes are zero
		compStrengthDayi = None
		cube1RemovedDayi = True
		cube2RemovedDayi = True #MRE Added
		cube3RemovedDayi = True #MRE Added
		commentsDayi = "Retest required for this sample"
		return compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi
	
	cube1.PSI = ScientificRounding.scientific_rounding(cube1.PSI, 0)  #-- MRE added for rounding/compare bug
	cube2.PSI = ScientificRounding.scientific_rounding(cube2.PSI, 0)  #-- MRE added for rounding/compare bug
	cube3.PSI = ScientificRounding.scientific_rounding(cube3.PSI, 0)  #-- MRE added for rounding/compare bug 

	if cube1.PSI >= minCube3 and cube1.PSI <= maxCube3:
		cube1.InRange = True

	if cube2.PSI >= minCube3 and cube2.PSI <= maxCube3:
		cube2.InRange = True

	if cube3.PSI >= minCube3 and cube3.PSI <= maxCube3:
		cube3.InRange = True

	if (cube1.InRange and cube2.InRange and cube3.InRange):
		return compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi

	#If not all in Range
	diff1 = abs(cube1.PSI - compStrengthDayi)
	diff2 = abs(cube2.PSI - compStrengthDayi)
	diff3 = abs(cube3.PSI - compStrengthDayi)

	cubeArray = [cube1.PSI, cube2.PSI, cube3.PSI]

	if (diff1 > diff2 and diff1 > diff3) or cube1.PSI == 0:
		cube1RemovedDayi = True
		load = '1'
		del cubeArray[0]
	elif (diff2 > diff1 and diff2 > diff3) or cube2.PSI == 0:
		cube2RemovedDayi = True
		load = '2'
		del cubeArray[1]
	else:
		cube3RemovedDayi = True
		load = '3'
		del cubeArray[2]

	compStrengthDayi = sum(cubeArray) / 2.0
	compStrengthDayi = ScientificRounding.scientific_rounding(compStrengthDayi, 0)
	deviation = compStrengthDayi * .076
	minCube2 = compStrengthDayi - deviation
	maxCube2 = compStrengthDayi + deviation

	if cubeArray[0] >= minCube2 and cubeArray[0] <= maxCube2 and cubeArray[1] >= minCube2 and cubeArray[1] <= maxCube2:
		commentsDayi= "Note: Adjusted Strength. Load %s Not Used."%load
	else:
		compStrengthDayi = None
		commentsDayi = "Retest required for this sample"

	return compStrengthDayi, cube1RemovedDayi, cube2RemovedDayi, cube3RemovedDayi, commentsDayi

class Cube():
	def __init__(self, cube):
		self.PSI = CheckValue(cube) / 4.0
		self.InRange = False

def CheckValue(entry):
	if entry is not None:
		return entry
	else:
		return 0