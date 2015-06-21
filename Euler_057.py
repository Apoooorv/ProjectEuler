from __future__ import division

numerator = 1
denominator = 2
count = 0

def continued_fraction():
	global numerator
	global denominator
	global count
	temp = numerator
	numerator = denominator
	denominator = 2*denominator+temp

	if len(str(numerator+denominator)) > len(str(denominator)):
		count += 1

for i in xrange(999):
	continued_fraction()

print count