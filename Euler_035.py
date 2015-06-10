def is_prime(n):
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True	

def generatecircularlist(number):
	circularnumber = str(number)
	returnlist = []
	for i in xrange(str(number).__len__()):
		circularnumber = (circularnumber[1:]) + (circularnumber[0])
		if int(circularnumber) == number or int(circularnumber) in returnlist:
			continue
		# if str(circularnumber).__len__() != str(number).__len__():
		# 	continue
		returnlist.append(int(circularnumber))
	return returnlist

primelist = []
for i in range(2, 1000000):
	if i in primelist:
		continue
	if is_prime(i):
		if i < 10:
			primelist.append(i)
			continue
		circularlist = generatecircularlist(i)
		flag = True
		for number in circularlist:
			if not is_prime(number) :
				flag = False
		if flag:
			primelist.append(i)
			for number in circularlist:
				if number not in primelist:
					primelist.append(number)

print primelist
print primelist.__len__()