# Author(s) Michael Elasky
# Date 6/11/2018
# Title ValidateTimeFormat
# Used Validate the Time Format
# Code version 1.00
# Type (Python Custom Module)

def validatetimeFormat(Repo,time):
	remark = None
	if time:
		if Repo.IsTime(time):
			remark = remark
		else:
			remark = 'Not Correct Time Format HH:mm'
	return remark
	
	
"""remark = None

if IsTime(Entity.StdMixTime):
   remark = remark
else:
   remark = 'Not Correct Time Format HH:mm or Legitimate Time Entered '

if remark is not None:
   raise Exception(remark)

Entity.TimeValidation = remark"""

#import sys
#sys.path.append('C:\AP_MnCustomScripts')
#from ValidateTimeFormat import *


#remark = validatetimeFormat(__RepoUtils,Entity.StdMixTime)

Entity.TimeValidation = None
remark = None

if Entity.StdMixTime:
   if IsTime(Entity.StdMixTime):
      remark = remark
   else:
      remark = 'Not Correct Time Format HH:mm or Legitimate Time Entered'

if remark is not None:
   raise Exception(remark)

Entity.TimeValidation = remark
	
		