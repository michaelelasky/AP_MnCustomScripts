# Author(s) Michael Elasky
# Date 4/27/2018
# Title GetSievesInSpec
# Used check in and out of specs on sieves
# Code version 1.00
# Type (Python Custom Module)

def getsievesinspec(chkwt=None,totaldrysamplewt_wtafterwash=None):
	compvalue = 0.3
	if chkwt and totaldrysamplewt_wtafterwash:
		chkinspec = (100*abs(float(chkwt - totaldrysamplewt_wtafterwash)/totaldrysamplewt_wtafterwash))
		if chkinspec <= compvalue:
			boolean = True
			inspec = 'In Spec'
		elif chkinspec > compvalue:
			boolean = False
			inspec = 'Out of Spec'
		else:
			inspec = 'No Spec'
		return inspec