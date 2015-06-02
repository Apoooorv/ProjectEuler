def fibNumber(number):
	if number == 0 :
		return 0
	elif number == 1:
		return 1
	else:
		return fibNumber(number - 1) + fibNumber(number-2)

i = 2
while True:
	if str(fibNumber(i)).__len__() == 1000:
		break
	i+=1

print i
