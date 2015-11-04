from flightTime import FTime

class Flight:
	def __init__(self, flNum, doa, crs, real):
		self.flNum = flNum
		self.isArrival = (doa == 0)
		self.crsTime = FTime(crs)
		self.realTime = FTime(real)
		if not isArrival: 	#dep
			self.startTime = crsTime.timeAfterDelay(-90)
			self.endTime = crsTime
		else: 	#arr
			self.startTime = crsTime
			self.endTime = crsTime.timeAfterDelay(45)

	def cmpEndTime(self, flight2):
		res = cmp(self.endTime, flight2.endTime)
