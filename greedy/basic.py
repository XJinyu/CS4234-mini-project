#unfinished
#Basic greedy algorithm
#----------------------
#Usage: modify path and file, run python filter.py
#Files should NOT include extension

#constants
path = "../data/2015-01/"
files = ["01-12478"]

#==================

def timeDiff(time1, time2):
	time1 = divmod(int(time1), 100)
	time2 = divmod(int(time2), 100)
	return (time2[0] - time1[0]) * 60 + time2[1] - time1[1]

def timeDelay(time, diff):
	time = divmod(int(time), 100)
	h = time[0]
	m = time[1]
	m += diff
	mid = divmod(m, 60)
	h += mid[0]
	m = mid[1]
	return str(h * 100 + m)

def process(file):
	pass
