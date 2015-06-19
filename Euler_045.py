from __future__ import division
import math

def is_pentagonal(n):
	root = math.sqrt(1+24*n)
	if not root.is_integer():
		return False
	value = (1 + root)/6
	if value.is_integer():
		return True
	return False

def is_triange(n):
	root = math.sqrt(1+8*n)
	if not root.is_integer():
		return False
	value = (root-1)/2
	if not value.is_integer():
		return False
	return True

def is_hexagonal(n):
	root = math.sqrt(1+8*n)
	if not root.is_integer():
		return False
	value = (root+1)/4
	if not value.is_integer():
		return False
	return True

for i in xrange(40756, 10000000000):
	if is_pentagonal(i) and is_triange(i) and is_hexagonal(i):
		print i
		break