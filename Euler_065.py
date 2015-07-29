def reciprocate():
	global num, den
	temp = num
	num = den
	den = temp

def add(n):
	global num, den
	num += n*den

def sum(n):
	string = str(n)
	addition = 0
	for i in xrange(len(string)):
		addition+=int(string[i])
	return addition

limit = 100

if limit == 1:
	num = 2

elif limit%3 != 0:
	num = 1

else:
	num = 2*(limit/3)

den = 1
prev = limit

for i in range(limit,1,-1):
	if i>2:
		if (i-1)%3 != 0:
			prev = 1
		else :
			prev = 2*((i-1)/3)
	else:
		prev = 2

	reciprocate()
	add(prev)
	# print i,current,num,den

print num, den
print sum(num)