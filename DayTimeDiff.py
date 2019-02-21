# Author(s) Michael Elasky
# Date 02/08/19
# Title DayTimeDiff
# Combines 2, day-time objects into datetime and calculates the duration between them then returns a day number,
# break message and day tolerance.
# Code version 5.00
# Type (Python Custom Module)


def combinedatetime(isdatei = None,istimei = None):
	import clr
	from System import DateTime
	from System import Convert
	
	dt= Convert.ToDateTime(isdatei + " " + istimei)
	return dt
	
def daysbetweenbreaks(mixdatei = None,mixtimei = None,breakdatei = None,breaktimei = None):
	from System import DateTime
	from System import TimeSpan
	from System import Convert
	
	daywithintolerance = False
	day = None
	dt = None
	break_message= 'Outside of time requirements '
	
	if mixdatei and mixtimei and breakdatei and breaktimei:
		mixdt=combinedatetime(mixdatei,mixtimei)
		breakdt=combinedatetime(breakdatei,breaktimei)
		if mixdt <= DateTime.Now and breakdt >= mixdt:
			dateduration = Convert.ToDateTime(breakdatei) - Convert.ToDateTime(mixdatei)
			dt = dateduration.Days
			duration = breakdt - mixdt
			durations = duration.TotalSeconds
			day = duration
			d=duration.Days
			h=duration.Hours
			m=duration.Minutes
			
			SECONDS_PER_MINUTE  = 60
			SECONDS_PER_HOUR    = 3600
			SECONDS_PER_DAY     = 86400
			dur = 0
	
			duration_in_sec = duration.TotalSeconds    # Total number of seconds between dates
			#84600-88200 24hr+-.5hr,255600-262800 d3+-1hr,594000-615600 d7+-3hrs,2376000-2462400 d28+-12hrs,4752000-4924800 d56+-24hrs
			seconds_range=[(84599, 88201),(255599, 262801),(593999,615601),(2375999, 2462401),(4751999, 4924801)]
			
			for sr in seconds_range:
				for r in sr:
					if duration_in_sec in range(sr[0],sr[1]):
						daywithintolerance = True
						break_message = 'Inside of time requirements'
						day=duration.Days
						if day == 0 or day == 2 or day == 6 or day == 27 or day == 55:
							day = day + 1
						elif day == 8 or day == 29 or day == 57:
							day = day - 1
						else:
							day = day
							
			if d <= 1 and dt <= 2:
				if durations < 84600:
					dur = 84600 - durations
				elif durations > 88200:
					dur = durations - 88200
			elif d >= 2 and dt <= 3 or dt == 4:
				if durations < 255600:
					dur = 255600 - durations
				elif durations > 262800:
					dur = durations - 262800
			elif d >= 6 and dt <= 7 or dt == 8:
				if durations < 594000:
					dur = 594000 - durations
				elif durations > 615600:
					dur = durations - 615600
			elif d >= 27 and dt == 28 or dt == 29:
				if durations < 2376000:
					dur = 2376000 - durations
				elif durations > 2462400 :
					dur = durations - 2462400 
			elif d >= 55 and dt == 56 or dt == 57:
				if durations < 4752000:
					dur = 4752000 - durations
				elif durations > 4924800:
					dur = durations - 4924800
			else:
				dur = durations

			days = dur / SECONDS_PER_DAY
			dur = dur % SECONDS_PER_DAY

			hours = dur / SECONDS_PER_HOUR
			dur = dur % SECONDS_PER_HOUR

			minutes = dur / SECONDS_PER_MINUTE
			dur = dur % SECONDS_PER_MINUTE
			
			d = int(dt)
			#d = int(days)
			h = int(hours)
			m = int(minutes)
				
			if daywithintolerance == True:
				day = str(day)
			elif h == 0 and m == 0:
				day=str(d)
			elif h == 0:
				day=str(d)+'     Mn:'+str(m)
			elif m == 0:
				day=str(d)+'     Hr:'+str(h)
			else:
				day=str(d)+'     Hr:'+str(h)+' Mn:'+str(m)
				
	return str(day), str(day), break_message, daywithintolerance