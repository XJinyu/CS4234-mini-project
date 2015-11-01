#Filter according to day and airport (one file per pair)
#----------------------
#Usage: modify path and file, run python filter.py
#Files should NOT include extension

#constants
path = "../data/"
file = "2015-01"

days = ["01"]
airports = ["12478"]

#==================

import os
import csv

def process(baseFile):
    readers = {}
    newpath = os.path.join(path, file)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for day in days:
        for airport in airports:
            key = day + "-" + airport
            filename = os.path.join(newpath, key + ".csv")
            readers[key] = open(filename, "w")

    with open(os.path.join(path, baseFile + '.csv'), 'rb') as csvfile:
        baseReader = csv.reader(csvfile)
        for row in baseReader:
            day = row[0][-2:]
            departure = row[2]
            arrival = row[3]
            if day + "-" + departure in readers:
                try:
                    flnum = row[1]
                    doa = 0
                    crstime = row[4]
                    realtime = row[5]
                    delay = row[6]
                    writer = csv.writer(readers[day + "-" + departure])
                    writer.writerow([flnum,doa,crstime,realtime,delay])
                except Exception, e:
                    pass
            if day + "-" + arrival in readers:
                try:
                    flnum = row[1]
                    doa = 1
                    crstime = row[7]
                    realtime = row[8]
                    delay = row[9]
                    writer = csv.writer(readers[day + "-" + arrival])
                    writer.writerow([flnum,doa,crstime,realtime,delay])
                except Exception, e:
                    pass

    for key, reader in readers.items():
        reader.close()

process(file)
