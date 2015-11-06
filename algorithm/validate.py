from flightTable import FlightTable

#validate
#assumptions:
#  All info in the table is inputted correctly
#  Flights in each gate are sorted by ending time

def validate(table):
	print "Validating..."
	validateSchedule(table)
	#validateDelay(table)
	

def validateSchedule(table):
	print "Correctness for scheduled time: "
	count = 0
	for index in range(len(table.gates)):
		if not table.validateGate(index):
			print "Gate " + str(index + 1) + " is incorrect:"
			table.printGate(index + 1)
			count += 1
	print str(count) + " gate(s) incorrect"

def validateDelay(table):
	print "After apply delay: "
	# TODO