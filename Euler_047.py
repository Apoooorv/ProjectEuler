def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

def factors(n):
	i = 1
	j = n
	factorlist = []
	while j > i:
		if (n%i == 0):
			if is_prime(i):
				factorlist.append(i)
			if is_prime(n/i):
				factorlist.append(n/i)
		j = n/i
		i+=1
	return factorlist


# print factors(644)
flag = False
for i in xrange(1,1000000):
	flag = False
	for j in xrange(4):
		factorlist = factors(i+j)
		if factorlist.__len__() != 4:
			flag = True
			break
	if not flag:
		print i
		break 