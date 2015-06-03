""" 
File for parsing total data transmitted 
in data packets.

NOTE: This code is a very early version,
and as such is not currently refined.
This will only work when fed a text file 
with all the information present. If extra
packets with MAC addresses that you do not 
want are in the text file, they will currently 
also be in the data set. If exporting from 
wireshark, make sure that both the Frame 
and Radiotap Header are expanded
"""
import os
import re
import sys

# You can input the file through command-line args
# Or you can just type it in
if len(sys.argv) > 1:
   f = open(sys.argv[1])
else:
   print "Enter file name"
   name = raw_input()
   f = open(name, 'r')

contents = f.read()
qosData = re.compile('QoS Data.{,}Data \(', re.DOTALL)
rate = re.compile('Data Rate: [0-9]*\.[0-9]')
dataRate = re.compile('[0-9]+ bytes on wire')
epochTime = re.compile('Epoch Time: [0-9]+\.[0-9]+')

allQoS = qosData.findall(contents)
joinedAllQoS = " ".join(allQoS)
allRates = rate.findall(joinedAllQoS)
allData = dataRate.findall(joinedAllQoS)
allTime = epochTime.findall(joinedAllQoS)

l =[]
p = []
m = []
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
  for q in allTime[x].split():
    try:
      m.append(float(q))
    except ValueError:
      pass

print "Total data transmitted (MB): " + str(sum(p)/(1024*1024))
print "Average data rate (Mb/s): " + str(sum(l)/float(len(l)))
print "Time taken: " + str(m[-1]-m[0])
