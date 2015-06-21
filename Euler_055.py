def is_lychrel(number):
	answer = number
	for i in xrange(50):
		answer += int(str(answer)[::-1])
		if str(answer) == str(answer)[::-1]:
			return False
	return True

count = 0

for i in xrange(1,10000):
	if is_lychrel(i):
		count+=1

print count