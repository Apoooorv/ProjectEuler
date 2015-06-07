import math

sequence = []
rangestart = 2
rangeend = 100
for i in range(rangestart, rangeend+1):
	for j in range(rangestart, rangeend+1):
		number = math.pow(i,j)
		if number not in sequence:
			sequence.append(number)

sequence.sort()
print sequence.__len__()