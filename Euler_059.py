import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(os.path.join(__location__,'Euler_059_data.txt'), 'r')

data = fp.read()
data = data.split(',')

def getKey(index):
	i = index
	EnKey = 97
	while i < data.__len__():
		xor = int(data[i])^EnKey
		if xor not in xrange(32,91) and xor not in xrange(97,123):
			i=index
			EnKey+=1
			continue
		i+=3
	return EnKey

array = [getKey(0), getKey(1), getKey(2)]

sum = 0
for i in xrange(data.__len__()):
	sum += (int(data[i])^array[i%3])

print sum