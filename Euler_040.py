string = []

for i in xrange(1,1000000):
	string.append(str(i))

string = ''.join(string)
multiplication = int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999])

print multiplication