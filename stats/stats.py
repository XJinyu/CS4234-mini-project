#Dependency: numpy
#Calculate stats
#----------------------
#Usage: modify path and files list, run python stats.py
#Files should NOT include extension

#Constants
path = "../data/"
files = ["2015-01"]

#==================

import os
import csv
import numpy

zero = 0
pos = numpy.zeros(11)
neg = numpy.zeros(11)
total = 0.0

def record(diff):
    global zero
    global pos
    global neg
    global total
    total += 1
    if diff == 0:
        zero += 1
    elif diff > 100:
        pos[10] += 1
    elif diff < -100:
        neg[10] += 1
    else:
        if diff > 0:
            pos[int(diff)/10] += 1
        else:
            neg[int(-diff)/10] += 1

def stat(reader):
    for row in reader:
        if float(row[10]) > 0:
            continue

        try:
            diff = float(row[6])
            record(diff)
        except Exception, e:
            pass

        try:
            diff = float(row[9])
            record(diff)
        except Exception, e:
            pass
        

for index, file in enumerate(files, start=1):
    print "{}: {}/{}".format("processing file", index, len(files))
    with open(os.path.join(path, file + '.csv'), 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        stat(spamreader)

print "----------"
print "{}: {}".format("nodelay", zero)
print "{}: {}".format("pos", pos)
print "{}: {}".format("neg", neg)

print "----------"
print "{}: {}".format("total", total)
print "stats:"
rneg = range(-10, 1)
rpos = range(1, 11)

def percent(x): 
    if x == 0:
        return "-"
    else:
        return "{0:.3f}".format(x/total)

formalNeg = list(reversed(neg))
statsNeg = map(percent, formalNeg)
statsPos = map(percent, pos)
print "<-10" +  '\t' + '\t'.join(str(v) for v in rneg)
print '\t'.join(statsNeg) + '\t' + "{0:.3f}".format(zero/total)
print '\t'.join(str(v) for v in rpos) + '\t' + ">10"
print '\t'.join(statsPos)

with open(os.path.join(path, "lastres.txt"), "w") as text_file:
    text_file.write("{}: {}".format("nodelay", zero) + '\n')
    text_file.write("{}: {}".format("pos", pos) + '\n')
    text_file.write("{}: {}".format("neg", neg) + '\n')
    text_file.write("----------" + '\n')
    text_file.write("{}: {}".format("total", total) + '\n')
    text_file.write("stats:" + '\n')
    text_file.write("<-10" +  '\t' + '\t'.join(str(v) for v in rneg) + '\n')
    text_file.write('\t'.join(statsNeg) + '\t' + "{0:.3f}".format(zero/total) + '\n')
    text_file.write('\t'.join(str(v) for v in rpos) + '\t' + ">10" + '\n')
    text_file.write('\t'.join(statsPos))

with open(os.path.join(path, "stats.csv"), "w") as csvfile:
    writer = csv.writer(csvfile)
    result = []
    result.extend(statsNeg)
    result.append("{0:.3f}".format(zero/total))
    result.extend(statsPos)
    writer.writerow(result)
