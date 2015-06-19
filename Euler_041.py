def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True	

def is_pandigital(number):
	if list(set(number)).__len__() == number.__len__():
		for i in xrange(1,number.__len__()+1):
			if number.find(str(i))==-1:
				return False
		return True
	return False

for i in xrange(987654321,100000000,-1):
	if is_pandigital(str(i)):
		if is_prime(i):
			print i
			break