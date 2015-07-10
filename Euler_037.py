def is_prime(n):
    i = 2
    if n < 2:
		return False
    while (i * i <= n):
        if (n % i == 0):
            return False
        i = i + 1   
    return True

def is_truncable(number):
	string = str(number)
	newstring = string
	for i in xrange(string.__len__()):
		if not is_prime(int(newstring)):
			return False
		newstring = newstring[1:]
	
	newstring = string
	for i in xrange(string.__len__()):
		if not is_prime(int(newstring)):
			return False
		newstring = newstring[:-1]
	return True


count = 0
truncableList = []
for i in xrange(10,1000000):
	if is_truncable(i):
		count+=1
		truncableList.append(i)
		if count == 11:
			break
print truncableList
print sum(truncableList)