def within5grams(trial1 = 0, trial2 = 0, trial3 = 0, trial4 = 0, trial5 = 0):
	if trial1 or trial2 or trial3 or trial4 or trial5:
		l = []
		#s = 'outside'
		r1 = range(trial1-5,trial1+5)
		r2 = range(trial2-5,trial2+5)
		r3 = range(trial3-5,trial3+5)
		r4 = range(trial4-5,trial4+5)
		r5 = range(trial5-5,trial5+5)
		if len(l)<3:
			l.append(trial1)
			if trial1 in r2:
				l.append(trial2)
				if len(l) == 5:
					return l
			if trial1 in r3:
				l.append(trial3)
				if len(l) == 5:
					return l
			if trial1 in r4:
				l.append(trial4)
				if len(l) == 5:
					return l
			if trial1 in r5 :
				l.append(trial5)
				if len(l) == 5:
					return l
		if len(l)<3:
			l = []
			l.append(trial2)
			if trial2 in r1:
				l.append(trial1)
				if len(l) == 5:
					return l
			if trial2 in r3:
				l.append(trial3)
				if len(l) == 5:
					return l
			if trial2 in r4:
				l.append(trial4)
				if len(l) == 5:
					return l
			if trial2 in r5:
				l.append(trial5)
				if len(l) == 5:
					return l
		if len(l)<3:
			l = []
			l.append(trial3)
			if trial3 in r1:
				l.append(trial1)
				if len(l) == 5:
					return l
			if trial3 in r2:
				l.append(trial3)
				if len(l) == 5:
					return l
			if trial3 in r4:
				l.append(trial4)
				if len(l) == 5:
					return l
			if trial3 in r5:
				l.append(trial5)
				if len(l) == 5:
					return l
		if len(l)<3:
			l = []
			l.append(trial4)
			if trial4 in r1:
				l.append(trial1)
				if len(l) == 5:
					return l
			if trial4 in r2:
				l.append(trial3)
				if len(l) == 5:
					return l
			if trial4 in r3:
				l.append(trial4)
				if len(l) == 5:
					return l
			if trial4 in r5:
				l.append(trial5)
				if len(l) == 5:
					return l
		if len(l)<3:
			l = []
			l.append(trial5)
			if trial5 in r1:
				l.append(trial1)
				if len(l) == 5:
					return l
			if trial5 in r2:
				l.append(trial2)
				if len(l) == 5:
					return l
			if trial5 in r3:
				l.append(trial3)
				if len(l) == 5:
					return l
			if trial5 in r4:
				l.append(trial4)
				if len(l) == 5:
					return l

		return l
		
def averofTries(*args):
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
			x = round(x/div,)
		else:
			raise Exception('fewer than 3 trials with 5 grams within each other')
		return x

