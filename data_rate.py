""" 
File for parsing total data transmitted 
in data packets.

NOTE: This code is a very early version,
and as such is not currently refined.
This will only work when fed a text file 
with all the information present. If extra
packets not meant to be included are in the
text file, they will currently also be in the
data set. If exporting from wireshark, make
sure that both the Frame and Radiotap Header
are expanded
"""
import os
import re
import sys

if len(sys.argv) > 1:
   f = open(sys.argv[1])
else:
   print "Enter file name"
   name = raw_input()
   f = open(name, 'r')

contents = f.read()
qosData = re.compile('QoS Data.{,}IEEE', re.DOTALL)
rate = re.compile('Data Rate: [0-9]*\.[0-9]')
dataRate = re.compile('[0-9]+ bytes on wire')

allQoS = qosData.findall(contents)
allRates = rate.findall(" ".join(allQoS))
allData = dataRate.findall(" ".join(allQoS))

l =[]
p = []

print 'Total packets: ' + str(len(allRates))

for x in range(len(allRates)):
    for t in allRates[x].split():
        try:
            l.append(float(t))
        except ValueError:
            pass
        
    for r in allData[x].split():
        try:
            p.append(float(r))
        except ValueError:
            pass

print "Total data transmitted (MB): " + str(sum(p)/(1024*1024))

print "Average data rate (Mb/s): " + str(sum(l)/float(len(l)))
