from flight import Flight
from flightTime import FTime

class FlightTable:
	def __init__(self):
		self.gates = []

	def totalGates(self):
		return len(self.gates)

	def assign(self, flight, gateNum):
		self.gates[gateNum].append(flight)
		self.gates.sort(lambda x, y: x.cmpEndTime(y))

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