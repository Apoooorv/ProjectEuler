import math

bigsum = 0
for i in range(2,1000000):
	string = str(i)
	sum = 0
	for j in range(string.__len__()):
		sum += math.pow(int(string[j]),5)
	if sum == i:
		bigsum+= i

print bigsum