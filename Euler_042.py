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
string = 'SKY'
sum = 0
for i in range(string.__len__()):
	sum+= ord(string[i]) - 64
print sum
for string in data:
	newstring = string[1:-1]
	sum = 0
	for i in range(string.__len__()):
		print ord(string[i])
		sum += ord(string[i])-64
	print sum
	if is_triangle(sum):
		count+=1
	break
print count
# 	break

# print count
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
# 	print str(number) + ' : ' + str(is_triangle(number))