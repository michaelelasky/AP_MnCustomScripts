# Author(s) Michael Elasky
# Date 6/14/2018
# Title FillEntityAttributeFieldResultsBM
# Module specific to Field Results BM(used in onsave)
# Code version 1.00
# Type (Python Custom Module)


def fillEntity(Entity,fieldresultslistSorted):	
	for index in range(0,len(fieldresultslistSorted)):
		if fieldresultslistSorted[index].Order == 1:
			Entity.MixAggBulkSpG = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 2:
			Entity.Neg4AggBulkSpG = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 3:
			Entity.AsphaltBinderSpG = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 4:
			Entity.FieldPerPass1Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 5:
			Entity.FieldPerPass3QuarterSieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 6:
			Entity.FieldPerPass5EighthsSieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 7:
			Entity.FieldPerPass1halfSieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 8:
			Entity.FieldPerPass3EighthsSieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 9:
			Entity.FieldPerPassNumber4Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 10:
			Entity.FieldPerPassNumber8Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 11:
			Entity.FieldPerPassNumber16Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 12:
			Entity.FieldPerPassNumber30Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 13:
			Entity.FieldPerPassNumber50Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 14:
			Entity.FieldPerPassNumber100Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 15:
			Entity.FieldPerPassNumber200Sieve = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 16:
			Entity.PerACIgnitionField = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 17:
			Entity.PerACChemExtrField = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 18:
			Entity.MaxSpGRice = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 19:
			Entity.BulkSpGgyratory = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 20:
			Entity.PerAirVoids = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 21:
			Entity.PerVMA = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 22:
			Entity.AdjustedAFT = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 23:
			Entity.FieldPer1FacedCrushed = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 24:
			Entity.FieldPer2FacedCrushed = fieldresultslistSorted[index].FieldData
		elif fieldresultslistSorted[index].Order == 25:
			Entity.FieldAvgPerFAA = fieldresultslistSorted[index].FieldData