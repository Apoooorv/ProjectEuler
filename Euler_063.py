
def is_ndigit(number,pow):
	mul = 1
	for i in xrange(pow):
		mul*=number
	if len(str(mul)) == pow:
		return True
	else:
		return False

count = 1
for i in xrange(2,100):
	for j in xrange(1,100):
		if is_ndigit(i,j):
			count+=1

print count