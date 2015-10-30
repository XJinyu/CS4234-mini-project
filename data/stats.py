#Usage: modify files list and run python stats.py

#constants
files = ["201501.csv"]

#==================

import csv
import numpy

zero = 0
pos = numpy.zeros(11)
neg = numpy.zeros(11)
total = 0.0

def stat(reader):
    global zero
    global pos
    global neg
    global total
    for row in reader:
        if float(row[10]) > 0:
            continue
        diff = float(row[6])
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
for file in files:
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        stat(spamreader)

print "----------"
print "{}: {}".format("nodelay: ", zero)
print "{}: {}".format("pos: ", pos)
print "{}: {}".format("neg: ", neg)

print "----------"
print "{}: {}".format("total: ", total)
print "stats:"
rneg = range(-10, 1)
rpos = range(1, 11)
print "<-10" +  '\t' + '\t'.join(str(v) for v in rneg)
formalNeg = list(reversed(neg))

def percent(x): 
    if x == 0:
        return "-"
    else:
        return str(float("{0:.2f}".format(x/total)))

statsNeg = map(percent, formalNeg)
statsPos = map(percent, pos)
print '\t'.join(statsNeg) + '\t' + str(zero/total)
print '\t'.join(str(v) for v in rpos) + '\t' + ">10"
print '\t'.join(statsPos)
