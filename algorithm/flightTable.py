from flight import Flight
from flightTime import FTime

class FlightTable:
	def __init__(self):
		self.gates = []

	def totalGates(self):
		return len(self.gates)

	def assign(self, flight, gateNum):
		self.gates[gateNum].append(flight)
		self.gates[gateNum].sort(lambda x, y: x.cmpEndTime(y))

	def assignToNewGate(self, flight):
		self.gates.append([flight])

	def gateWithLatestEnding(self):
		latest = -1
		latestTime = FTime(0, 0)
		for index, gate in enumerate(self.gates):
			if gate[-1].endTime > latestTime:
				latestTime = gate[-1].endTime
				latest = index
		return (latest, latestTime)

	def latestAvailableGateForFlight(self, flight):
		latest = -1
		latestTime = FTime(0, 0)
		for index, gate in enumerate(self.gates):
			if gate[-1].endTime > latestTime and gate[-1].endTime < flight.startTime:
				latestTime = gate[-1].endTime
				latest = index
		return (latest, latestTime)

	def validateGate(self, gateNum):
		gate = self.gates[gateNum]
		for index in range(len(gate) - 1):
			if gate[index].endTime > gate[index + 1].startTime:
				return False
		return True

	def printGates(self):
		print "Total gates: " + str(self.totalGates())
		for index, gate in enumerate(self.gates):
			flightNums = []
			map(lambda flight: flightNums.append(flight.flNum), gate)
			print "Gate " + str(index + 1) + ": " + ", ".join(flightNums)

	def printGate(self, gateNum):
		gateNum -= 1
		print "Gate " + str(gateNum + 1) + "/" + str(len(self.gates))
		for flight in self.gates[gateNum]:
			print "Flight " + flight.flNum.zfill(5) + ": " + flight.startTime.toStr() + " to " + flight.endTime.toStr()

