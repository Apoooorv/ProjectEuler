def is_following(number, index):
	string = str(number)
	sum = 0
	for char in string:
		sum+=int(char)
	if sum == index:
		return True
	return False

count = 0
array = []
for i in xrange(2,100):
	for j in xrange(1,50):
		power = i**j
		if power < 10:
			continue
		if is_following(power,i):
			count+=1
			array.append(power)
		if count == 30:
			break

array.sort()
print array[29]