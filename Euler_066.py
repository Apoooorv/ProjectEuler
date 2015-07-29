import math

def findx(number):
	if math.sqrt(number).is_integer():
		return 0
	else:
		for i in xrange(1,100000000):
			square = 1 + number*i*i
			if math.sqrt(square).is_integer():
				return math.sqrt(square)

	return None

max = 0
number = 0
for i in xrange(2,1001):
	print i
	ans = findx(i)
	if ans > max:
		max = ans
		number = i

print max
print number