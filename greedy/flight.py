from flightTime import FTime

class Flight:
	def __init__(self, flNum, doa, crs, real):
		self.flNum = flNum
		self.isArrival = (int(doa) == 0)
		self.crsTime = FTime(crs)
		self.realTime = FTime(real)
		self.delay = self.realTime.minus(self.crsTime)
		if not self.isArrival: 	#dep
			self.startTime = self.crsTime.timeAfterDelay(-90)
			self.endTime = self.crsTime
		else: 	#arr
			self.startTime = self.crsTime
			self.endTime = self.crsTime.timeAfterDelay(45)

	def cmpEndTime(self, flight2):
		return cmp(self.endTime, flight2.endTime)
