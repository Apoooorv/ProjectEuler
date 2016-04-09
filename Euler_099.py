from __future__ import division
import os, math

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(os.path.join(__location__,'Euler_099_data.txt'), 'r')

data = fp.read()

data = data.split('\n')

maxval = 0
answer = 0
for i in xrange(0,data.__len__()):
	var = data[i].split(',')
	log = int(var[1])*math.log10(int(var[0]))
	if log > maxval:
		maxval = log
		result = i

print result + 1