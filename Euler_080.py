from decimal import *

def calculate_sum(n):
	getcontext().prec = 105
	i = Decimal(n).sqrt()
	if i%1 == 0:
		return 0
	p = pow(10, 99)
	i*=p
	array = str(i)[:100]
	sum = 0
	if array:
		for char in array:
			sum += int(char)
	return sum

sum = 0
for i in xrange(2,101):
	sum += calculate_sum(i)
print sum