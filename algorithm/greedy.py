#Basic greedy algorithm
#Dependency: numpy
#----------------------
#Usage: modify path and file, run python filter.py
#Files should NOT include extension

#constants
path = "../data/2015-01/"
file = "01-12478"
minInterval = 0

#==================
import os
import numpy as np
import csv

# folder as module
__all__ = ['flight', 'flightTable', 'flightTime', 'validate']

from modules.flightTable import FlightTable
from modules.flight import Flight
from modules.flightTime import FTime
from modules.validate import *

flights = []
flightTable = FlightTable()

def inputFrom(path, file): 
	with open(os.path.join(path, file+'.csv'),'rb') as csvfile:
		basic_reader = csv.reader(csvfile)
		for row in basic_reader:
			#fl_num,dep(0)/arr(1),crs_time,real_time, delay
			flights.append(Flight(row[0], row[1], row[2], row[3], minInterval)) 
	flights.sort(lambda x, y: x.cmpEndTime(y))
		
def greedyAllocate(flights, table):
	for flight in flights:
		gate, _ = table.latestAvailableGateForFlight(flight)
		if gate == -1:
			table.assignToNewGate(flight)
		else:
			table.assign(flight, gate)

inputFrom(path, file)

greedyAllocate(flights, flightTable)

validate(flightTable, os.path.join(path, file+'.csv'))

# flightTable.printGate(1)


