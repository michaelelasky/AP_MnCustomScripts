# Author(s) Mike Elasky
# Date 02/20/2019
# Title ExceptionCode
# used to catch required fields and through an exception
# Code version 1.00
# Type (Python Custom Module)

def exceptionCode(uniquefield,**kwargs):
	if uniquefield is not None:
		entityattribute = ''
		comma = ''
		punctuation = 'is'
		error = None
		errormessage = ''
		count = 0
		if kwargs is not None:
			for key, value in kwargs.items():
				if value is None or value == '':
					count = count + 1
					entityattribute = key
					error = True
					if count > 1:
						comma = ', '
						if count > 1:
							punctuation = 'are'
					else:
						comma = ''
					errormessage = errormessage  + comma + entityattribute
			#if error:
				#er = '%s %s Required'%(errormessage,punctuation)
				#raise Exception(er)