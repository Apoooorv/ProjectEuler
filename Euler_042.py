from __future__ import division
import os
import math

def is_triangle(number):
	root = math.sqrt(1+8*number)
	if not root.is_integer():
		return False
	value = (root-1)/2
	if not value.is_integer():
		return False
	return True

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(os.path.join(__location__,'Euler_042_data.txt'), 'r')

data = fp.read()
data = sorted(data.split(','))

count = 0

for string in data:
	newstring = string[1:-1]
	sum = 0
	for i in range(newstring.__len__()):
		sum += ord(newstring[i])-64
	if is_triangle(sum):
		count+=1
print count