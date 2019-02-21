# Author(s) Michael Elasky
# Date 2/23/18
# Title InOutOfSpec
# Used to determine if a value is within given spec.
# Code version 1.00
# Type (Python Custom Module)


def inoutofSpec(materialtestvalue=None,targetvalue=None,positivetargetdeviation=None,negativetargetdeviation=None,maxlimit=None,minlimit=None):
	if materialtestvalue is None:
		return
	matvalue = materialtestvalue
	specmessage = 'In Spec'
	if not targetvalue and not positivetargetdeviation and not negativetargetdeviation and not maxlimit and not minlimit:
		return 'No Spec'
	if minlimit or maxlimit:
		min = minlimit
		max = maxlimit
	elif targetvalue and positivetargetdeviation and negativetargetdeviation:
		min = targetvalue - negativetargetdeviation
		max = targetvalue + positivetargetdeviation
	else:
		return
	if min and max:
		if not matvalue >= min or not matvalue <= max:
			specmessage = 'Out of Spec'
	if min and not max:
		if not matvalue >= min:
			specmessage = 'Out of Spec'
	if max and not min:
		if not matvalue <= max:
			specmessage = 'Out of Spec'
	return specmessage
