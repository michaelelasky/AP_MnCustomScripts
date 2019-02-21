# Author(s) Michael Elasky
# Date 08/17/2018
# Title AverOfTries
# used to get list data and calculate average of at least 3 numbers within 5g of eachother
# Code version 1.00
# Type (Python Custom Module)

def within5grams(m,*args):
	l = []
	trial = []
	a = 0
	b = 0
	if args:
		for arg in args:
			x = arg
			trial.append(x)
		for t in trial:
			l = []
			l.append(trial[a])
			for t in trial:
				if a != b:
					if trial[a] in range(trial[b]-m,trial[b]+m):
						l.append(trial[b])
				b = b + 1
			if len(l) >=3:
				return l
			a = a + 1
			b = 0
		return l
		
def averofTries(m,*args):
	argsv = []
	for arg in args:
		if arg is not None:
			argsv.append(arg)
	items = within5grams(m,*argsv)
	x = 0
	if items:
		div=len(items)
		if div >= 3:
			for item in items:
				x = x + item
			x = round(x/div,0)
		else:
			raise Exception('Fewer than 3 trials with  5 grams range within them')
			
		return x

