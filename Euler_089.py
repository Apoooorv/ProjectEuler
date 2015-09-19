import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(os.path.join(__location__,'Euler_089_data.txt'), 'r')

data = fp.read()

data = data.split('\n')

stringarray = ['I','V','X','L','C','D','M']
numberarray = [1, 5, 10, 50, 100, 500, 1000]

def getnumber(string):
	global array
	decimalnumber = 0
	flag = False
	for i in range(len(string)):
		# print flag, decimalnumber, string[i]
		if flag :
			flag = False
			continue
		else:
			if i < len(string)-1 and stringarray.index(string[i]) % 2 == 0:
				nextelement = stringarray.index(string[i+1]) - stringarray.index(string[i])
				if nextelement == 1 or nextelement == 2:
					flag = True
					decimalnumber += (numberarray[stringarray.index(string[i+1])] - numberarray[stringarray.index(string[i])])
					continue
				else :
					decimalnumber += numberarray[stringarray.index(string[i])]
			else :
				decimalnumber += numberarray[stringarray.index(string[i])]

	return decimalnumber

def getstring(number):
	tempnumber = number
	string = ''
	index = len(numberarray)
	while True:
		index = index - 1
		# print tempnumber, numberarray[index], string
		if index % 2 == 1:
			if tempnumber / numberarray[index-1] == 9:
				string += stringarray[index-1] + stringarray[index+1]
				tempnumber -= (numberarray[index+1]-numberarray[index-1])
				continue
			elif tempnumber / numberarray[index] == 4:
				string += stringarray[index-1] + stringarray[index]
				tempnumber-= (numberarray[index]-numberarray[index-1])
				continue
			else :
				pass
		if tempnumber == 0:
			break

		value = tempnumber/numberarray[index]
		
		if not value:
			continue
		if value == 4 and index != len(numberarray)-1:
			string = string + stringarray[index] + stringarray[index+1]
		else:
			for i in xrange(value):
				string = string + stringarray[index]
		tempnumber-=value*numberarray[index]
	return string

saving = 0
arr = []
for number in data:
	i = getnumber(number)
	j = getstring(i)
	save = len(number) - len(j)
	saving += save
	# print number, i, j, save

print saving