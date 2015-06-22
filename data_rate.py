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
   f = open(name)

contents = f.read()

qosData = re.compile('TCP segment data \([0-9]+') #looking for TCP segment data
rate = re.compile('Data Rate: [0-9]*\.[0-9]')
dataRate = re.compile('[0-9]+ bytes on wire')
epochTime = re.compile('Epoch Time: [0-9]+\.[0-9]+')

allQoS = qosData.findall(contents)
allRates = rate.findall(contents)
allData = qosData.findall(contents)
allTime = epochTime.findall(contents)

l =[]
p = []
m = []
print 'Total packets: ' + str(len(contents))
for i in range(0,len(allTime)):
    print(allTime[i])
    t = allTime[i].split(' ')
    m.append(float(t[2]))

print("length: " + str(len(allData)))
for j in range(0,len(allData)):
    print(allData[j])
    data = allData[j].split(' ')
    data[3] = data[3][1:]
    print(data[3])
    p.append(int(data[3]))

print(str(sum(p)))
print "Total data transmitted (MB): " + str((sum(p)/1000))
print "Average data rate (Mb/s): " + str(((sum(p))/(1000))/(m[-1]-m[0]))
print "Time taken: " + str(m[-1]-m[0])
