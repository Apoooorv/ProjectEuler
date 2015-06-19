import itertools

def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

def is_increasing(i):
	number_list = []
	numbers = list(itertools.permutations(str(i)))
	for number in numbers:
		permutation = int(''.join(number))
		if is_prime(permutation):
			number_list.append(permutation)
	
	flag = 0
	number_list = list(set(number_list))
	if len(number_list)<3 :
		return ''
	number_list.sort()
	for i in xrange(number_list.__len__()):
		for j in xrange(i+1,number_list.__len__()):
			difference = number_list[j] - number_list[i]
			if (number_list[j]+difference) in number_list:
				return str(number_list[i])+str(number_list[j])+str(number_list[j]+difference)
	return ''

primelist = []
for i in xrange(1000,10000):
	string = is_increasing(i)
	if string and len(string)==12:
		primelist.append(string)

primelist = list(set(primelist))
print primelist