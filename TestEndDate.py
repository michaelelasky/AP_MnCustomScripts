# Author(s) Michael Elasky
# Date 4/27/2018
# Title TestEndDate
# Used to calculate an end date by number of days
# Code version 1.00
# Type (Python Custom Module)

def TestEndDate(start_date,numofDays):
	import clr
	from System import DateTime
	from System import TimeSpan
	from datetime import datetime, timedelta, date
	date_1=datetime.strptime(start_date,'%m/%d/%Y %H:%M:%S %p')
	end_date = date_1 + timedelta(days=numofDays)
	return end_date.strftime('%m/%d/%Y %H:%M:%S %p')