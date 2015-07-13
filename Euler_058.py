from __future__ import division

def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

answer = 0
current = 1
primecount = 0
totalcount = 1

for i in xrange(1,100000):
	for j in xrange(4):
		current+=2*i
		if is_prime(current):
			primecount+=1
	totalcount+=4
	if primecount/totalcount < 0.1:
		answer = i
		break

print 2*answer + 1
