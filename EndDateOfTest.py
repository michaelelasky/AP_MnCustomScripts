# Author(s) Michael Elasky
# Date 5/3/18
# Title EndDateOfTest
# Calculates test end date from number of days past starting date.
# Code version 1.00
# Type (C# Custom Module)

def gettestendDate(startDate,numofDays):
	import clr
	from System import DateTime
	endDate = None
	if startDate is not None:
		parsedDate = DateTime.Parse(startDate)
		endDate = parsedDate.AddDays(numofDays)
	return endDate