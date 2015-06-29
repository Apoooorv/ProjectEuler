def is_following(numerator, number):
	if (numerator*number)%(numerator-number)==0:
		return True
	return False

biggest = 0
for number in xrange(1000000):
	
	count = 0
	for i in xrange(number+1,(2*number)+1):
		if is_following(i,number):
			count+=1

	print number, count
	if count > 1000:
		biggest = count
		answer = number
		break
	if count > biggest:
		biggest = count
		answer = number

print biggest 
print answer