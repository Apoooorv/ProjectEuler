import math

def get_sum(num,pow):
	sum = 0
	mul = 1
	for i in xrange(pow):
		mul*=num
	string = str(mul)
	for char in string:
		sum+=int(char)
	return sum
	
biggest = 0
for i in xrange(2,100):
	for j in xrange(2,100):
		sum = get_sum(i,j)
		if sum > biggest:
			biggest = sum

print biggest