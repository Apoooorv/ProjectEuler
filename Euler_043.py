def is_divisible(number):
	primelist=[2,3,5,7,11,13,17]
	string = str(number)
	for i in xrange(1,8):
		substring = string[i:(i+3)]
		if int(substring)%primelist[i-1] != 0:
			return False
	return True


def is_pandigital(number):
	if list(set(number)).__len__() == 10:
		return True
	return False

numberlist = []
# print is_divisible(1406357289)
for i in xrange(1023456789,10000000000):
	if is_pandigital(str(i)):
		if is_divisible(i):
			numberlist.append(i)

print numberlist
print sum(numberlist)