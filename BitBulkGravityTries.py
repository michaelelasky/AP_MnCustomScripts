# Author(s) Nicholas Nyakundi
# Date 12/13/2018
# Title BitBulkGravityTries
# used to get list data and calculate average of at least 2 numbers within 0.020g of each other
# Code version 1.00
# Type (Python Custom Module)

#import bitrange as xy

from bitrange import *

def within2grams(*args):
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
					
					if trial[a] in bitrange((trial[b]-0.02),(trial[b]+0.02),0.001):
						
						l.append(trial[b])
				b = b + 1
			if len(l) >=2:
				return l
			a = a + 1
			b = 0
		return l
		
def BitBulkGravityTries(*args):
	argsv = []
	for arg in args:
		if arg is not None:
			argsv.append(arg)
	items = within2grams(*argsv)
	x = 0.0
	if items:
		div=len(items)
		if div >= 2:
			
			for item in items:
				x = x + item
			
			x = round(x/div,3)
		else:
			raise Exception('Fewer than 2 trials with  0.020 grams range within them')
			
		return x

