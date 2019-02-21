# Author(s) Nicholas Nyakundi
# Date 12/13/2018
# Title AverOfTries
# used to get list data and calculate average of at least 3 numbers within 5g of eachother
# Code version 2.00
# Type (Python Custom Module)

def within5grams(*args):
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
					if trial[a] in range(trial[b]-5,trial[b]+5):
						l.append(trial[b])
				b = b + 1
			if len(l) >=3:
				return l
			a = a + 1
			b = 0
		return l
		
def averofTried(*args):
	argsv = []
	for arg in args:
		if arg is not None:
			argsv.append(arg)
	items = within5grams(*argsv)
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

