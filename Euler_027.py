def is_prime(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return False
        i = i + 1   
    return True

def checksum(sum, product):
	for i in range(product+1):
		equation = (i*i) + (sum*i) + product
		if equation < 0 or not is_prime(equation):
			return i

maxrange = 0
maxproduct = 1
for sum in xrange(-1000,1001):
	for product in xrange(1001):
		if is_prime(product):
			primerange = checksum(sum, product)
			if primerange > maxrange:
				maxrange = primerange
				maxproduct = sum*product

print maxrange
print maxproduct