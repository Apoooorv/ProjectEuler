productlist = []

for i in xrange(1,100):
	for j in xrange(100,10000):
		product = i*j
		newlist = []
		newlist.extend((str(i),str(j),str(product)))
		string = ''.join(newlist)
		if string.__len__() == 9:
			if list(set(string)).__len__() == 9:
				if string.find('0') != -1:
					pass
				else:
					productlist.append(product)

productlist = list(set(productlist))
print sum(productlist)

