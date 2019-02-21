# Author(s) Nicholas Nyakundi
# Date 08/29/2018
# Title AverOfTrials
# used to get list data and calculate average of at least 3 numbers within 25g of eachother
# Code version 1.00
# Type (Python Custom Module)

def within25grams(*args):
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
					if trial[a] in range(trial[b]-25,trial[b]+25):
						l.append(trial[b])
				b = b + 1
			if len(l) >=3:
				return l
			a = a + 1
			b = 0
		return l
		
def averofTrials(*args):
	argsv = []
	for arg in args:
		if arg is not None:
			argsv.append(arg)
	items = within25grams(*argsv)
	x = 0
	if items:
		div=len(items)
		if div >= 3:
			for item in items:
				x = x + item
			x = round(x/div,0)
		else:
			raise Exception('Fewer than 3 trials with  25 grams range within them')
			
		return x

