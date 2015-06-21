from __future__ import division
import math

def equation(n):
	root = math.sqrt(1+24*n)
	number = (1 + root)/6
	if number.is_integer():
		return True
	return False

lowest = 10000000
for i in xrange(10000000):
	if equation(i):
		for j in xrange(i+1,10000000):
			if equation(j):
				if equation(i+j) and equation(j-i):
					if j-i < lowest:
						lowest = j-i

print lowest