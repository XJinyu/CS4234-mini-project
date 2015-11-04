#Basic greedy algorithm
#Dependency: numpy
#----------------------
#Usage: modify path and file, run python filter.py
#Files should NOT include extension

#constants
path = "../data/2015-01/"
file = "01-12478"

#==================
import os
import numpy as np
import csv

def process(path,file): 
	with open(os.path.join(path, file+'.csv'),'rb') as csvfile:
		basic_reader = csv.reader(csvfile)
		rows = list(basic_reader)
		row_count = len(rows)
		flights = np.zeros((row_count,5)) #fl_num,dep(0)/arr(1),crs_time,empty
		for i,row in enumerate(rows):
			flights[i,:-2]=np.array([int(row[0]),int(row[1]),int(row[2])])
		return flights,row_count
	
def convertToInterval(flights,row_count):	  #process flights info, add start time and end time for each flight, convert hhmm to minutes
	for i in range(row_count):
		if (flights[i,1]==0): #dep
			crs_time = int(flights[i,2])
			flights[i,3]=(int(crs_time)/100)*60 + (int(crs_time)%100)-90
			flights[i,4]=flights[i,3]+100
		else : #arrival
			crs_time = flights[i,2]
			flights[i,3]=(int(crs_time)/100)*60 + (int(crs_time)%100)
			flights[i,4]=flights[i,3]+45
	return flights
		
def greedyAllocate(gates,gates_pointer,flights,total_flights):
	flights = flights[flights[:,3].argsort()]  #sort according to start time 
	gate_index = -1
	for i in range(total_flights):
		allocated = 0
		for j in range(gate_index+1):
			if (allocated==0) and (flights[i,3]>gates_pointer[j]):
				for k in range(gate_capacity):
					if (gates[j,k,2]==0) and (allocated==0):
						gates[j,k,:]=flights[i,:-2]
						gates_pointer[j]=flights[i,4]
						allocated = 1
		if (allocated==0):
			gate_index = gate_index+1
			gates_pointer[gate_index]=flights[i,4]
			gates[gate_index,0,:]=flights[i,:-2]
	return gates,gate_index+1

flights,total_flights = process(path,file)
flights = convertToInterval(flights,total_flights)

gate_size = 600                #initialize 100 available gates
gate_capacity = (24*60+45)/45    #max number of planes a gate can host
gates_schedule = np.zeros((gate_size,gate_capacity,3))            
gates_pointer = np.zeros(gate_size)

gates_schedule,gate_used = greedyAllocate(gates_schedule,gates_pointer,flights,total_flights)

print gate_used

