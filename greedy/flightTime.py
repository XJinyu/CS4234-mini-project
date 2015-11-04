class FTime:
	def __init__(self, arg1, arg2 = None):
		if arg2 is None and type(arg1) is str:
			time = divmod(int(str), 100)
			self.hours = time[0]
			self.mins = time[1]
		else: 
			try:
				hours = int(arg1)
				mins = int(arg2)
			except Exception, e:
				print e
				raise

	def toStr(self):
		return str(self.hours * 100 + self.mins)

	def minus(self, time2):
		time2 = divmod(int(time2), 100)
		return (self.selfhours - time2[0]) * 60 + self.mins - time2[1]

	def delay(self, diff):
		newTime = timeAfterDelay(diff)
		self.hours = newTime.hours
		self.mins = newTime.mins

	def timeAfterDelay(self, diff):
		h = self.hours
		m = self.mins
		m += diff
		mid = divmod(m, 60)
		h += mid[0]
		m = mid[1]
		return FTime(h, m)

	def __cmp__(self, obj):
		if not isinstance(obj, FTime):
			return -1
		
		res = self.minus(obj)
		if res < 0:
			return -1
		elif res > 0:
			return 1
		else:
			return 0

