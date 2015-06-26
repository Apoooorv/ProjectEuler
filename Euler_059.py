import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(os.path.join(__location__,'Euler_059_data.txt'), 'r')

data = fp.read()
data = data.split(',')

flag = False
values = []

EnKeyi = EnKeyj = EnKeyk = 97
i = 0
while i <= data.__len__():
	print EnKeyi
	if EnKeyi > 122:
		print 'Not found'
		break
	xor = EnKeyi ^ int(data[i])
	print data[i],int(data[i]),xor
	# print data[i],int(data[i]),EnKeyi,xor
	if (xor>122) or (xor<65):
		print values
		i = 0
		values = []
		EnKeyi+=1
	else:
		values.append(xor)
		i+=3

print values