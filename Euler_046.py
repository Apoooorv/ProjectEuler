import math

def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True	

flag = False
for i in xrange(3,10000000,2):
	if not is_prime(i):
		for j in range(1,i,2):
			if is_prime(j):
				number = math.sqrt((i-j)/2)
				if number.is_integer():
					flag = True
					break
		if not flag:
			print i
			break