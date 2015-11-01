#unfinished
#----------------------
#Usage: modify path and files list, run python filter.py
#files should NOT include extension
#constants
path = "../data/"
files = ["2015-01"]

days = []
airports = []

#==================

import os
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

