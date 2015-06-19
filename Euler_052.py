def is_same_multiple(number):
	string = list(str(number))
	string.sort()
	for i in xrange(2,7):
		newnumber = number*i
		newstring = list(str(newnumber))
		newstring.sort()
		if string != newstring:
			return False

	return True

# print is_same_multiple(125874)
for i in xrange(1,1000000):
	if is_same_multiple(i):
		print i
		break