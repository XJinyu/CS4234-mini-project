from flightTime import FTime

class Flight:
	def __init__(self, flNum, doa, crs, real, extend = 0):
		preDep = 90
		extDep = 10 + extend
		extArr = 45 + extend
		self.flNum = flNum
		self.isArrival = (int(doa) == 1)
		self.crsTime = FTime(crs)
		self.realTime = FTime(real)
		self.delay = self.realTime.minus(self.crsTime)
		if not self.isArrival: 	#dep
			self.startTime = self.crsTime.timeAfterDelay(-preDep)
			self.endTime = self.crsTime.timeAfterDelay(extDep)
		else: 	#arr
			self.startTime = self.crsTime
			self.endTime = self.crsTime.timeAfterDelay(extArr)
		self.delayedStartTime = self.startTime.timeAfterDelay(self.delay)
		self.delayedEndTime = self.endTime.timeAfterDelay(self.delay - extend)

	def cmpEndTime(self, flight2):
		return cmp(self.endTime, flight2.endTime)
