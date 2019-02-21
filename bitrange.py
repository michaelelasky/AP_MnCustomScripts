
def bitrange(start,stop,step):
	r = start
	while r < stop:
		yield r
		r += step

