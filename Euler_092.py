def condition_satisfies(number):
	addition = number
	while 1:
		if addition == 1:
			return False
		elif addition == 89:
			return True
		else:
			string = str(addition)
			addition = 0
			for i in string:
				addition+=int(i)*int(i)

count = 0
for i in xrange(1,10000000):
	if condition_satisfies(i):
		count+=1

print count