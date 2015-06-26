def rmax(number):
	square = number**2
	greatest = 0
	for i in xrange(1,10000):
		result = (number-1)**i + (number+1)**i
		mod = result%square
		if mod > greatest:
			greatest = mod
	return greatest

# print rmax(7)
sum=0
for i in xrange(3,1001):
	sum1 = rmax(i)
	print i, sum1
	sum+=sum1

print sum