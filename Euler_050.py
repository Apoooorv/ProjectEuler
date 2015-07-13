def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

def count(n):
	for i in xrange(2,n):
		primelist = []
		sum = 0
		for j in xrange(i,n):
			if is_prime(j):
				sum+=j
				primelist.append(j)
				if sum == n:
					return primelist.__len__()
				if sum > n:
					break
	return 0

max = 0
number = 0
for i in xrange(2,1000000):
	primecount = count(i)
	if primecount > max:
		max = primecount
		number = i

print max
print number