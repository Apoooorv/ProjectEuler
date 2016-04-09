def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

limit = 1000000
multiplication = 1
for i in xrange(1,25):
	if is_prime(i):
		multiplication = multiplication*i
		if multiplication > limit:
			multiplication = multiplication/i
			break

print multiplication