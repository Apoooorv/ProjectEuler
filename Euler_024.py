import math

print math.factorial(10)

number = 0
threshold = 1
listrange = 3
combination = []
sum = 0
i = 0
while i<listrange:
	print i
	for j in range(listrange):
		if j not in combination:
			if sum + (j+1)*math.factorial(listrange-i-1) > threshold:
				print j
				print (j+1)*math.factorial(listrange-i-1)
				combination.append(j)
				sum += j*math.factorial(listrange-i-1)
				i+=1
				break

print combination