# Author(s) Mike Elasky
# Date 02/19/2019
# Title PercentFiner
# Used to calc percent finer on #20 sieve
# Code version 1.00
# Type (Python Custom Module)

def percentFiner(weightretain2In, weightretain1In, weightretain3_4In, weightretain3_8In, weightretainNo4, totalcoarseWt,\
					weightretainNo10, weightretainbottomMed, weightretainedonNum20, weightretainedonNum40, weightretainedonNum60,\
					weightretainedonNum100, weightretainedonNum200, origsampleWeight, hygroscopicmoistureCorrection)
	percentfiner = None
	weightretained = None
	weightretained = (weightretain2In + weightretain1In + weightretain3_4In + weightretain3_8In + weightretainNo4) * 100
	
	
	
