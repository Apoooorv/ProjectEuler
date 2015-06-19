def is_pandigital(number):
	if list(set(number)).__len__() == 9:
		if number.find('0') == -1:
			return True
	return False

greatest = 0
for i in xrange(1,100000):
	product = []
	for j in xrange(1,10):
		product.append(str(i*j))
		productstring = ''.join(product)
		if productstring.__len__() == 9:
			if is_pandigital(productstring) and j>1:
				if int(productstring) > greatest:
					greatest = int(productstring)
					number = i
					multiplier = j
			break

print greatest