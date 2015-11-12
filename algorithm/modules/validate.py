from flightTable import FlightTable
import csv

#validate
#assumptions:
#  All info in the table is inputted correctly
#  Flights in each gate are sorted by ending time

def validate(table, dataFile):
	print "Used " + str(len(table.gates)) + " gate(s)"
	validateSchedule(table)
	validateDelay(table, dataFile)
	

def validateSchedule(table):
	count = 0
	for index in range(len(table.gates)):
		if not table.validateGate(index):
			print "Warning: Schedule for gate " + str(index + 1) + " is incorrect:"
			table.printGate(index + 1)
			count += 1

def validateDelay(table, dataFile):
	with open(dataFile, "rb") as csvfile:
		reader = csv.reader(csvfile)
		count = 0
		for index in range(len(table.gates)):
			clash = table.validateGateDelayed(index)
			# print "Gate " + str(index + 1) + ": " + str(clash) + " clash(es)"
			count += clash
		print "Total " + str(count) + " clash(es)"

	