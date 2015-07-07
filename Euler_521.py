def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

def smpf(n):
	if is_prime(n):
		return n
	for i in xrange(2,n):
		if n%i == 0 and is_prime(i):
			return i
	return 0

sum = 0
for i in xrange(1,10**12+1):
	sum+=smpf(i)

print sum
print sum % (10**9)