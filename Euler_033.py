from __future__ import division

def is_common(num,den):
	if num == den:
		return False
	if num%11 == 0 or den%11==0:
		return False

	numerator = str(num)
	denominator = str(den)

	for i in xrange(1,10):
		if numerator.find(str(i))!=-1 and denominator.find(str(i))!=-1:
	
			newnumerator = int(numerator.translate(None,str(i)))
			newdenominator = int(denominator.translate(None,str(i)))

			if not newdenominator == 0:
				if newnumerator/newdenominator == num/den and newnumerator < newdenominator:
					return True			
	return False


commonlist = []
numerator = 1
denominator = 1
for i in xrange(10,100):
	for j in xrange(10,100):
		if is_common(i,j):
			numerator *= i
			denominator *= j

for num in range(numerator,1,-1):
	if numerator%num == 0 and denominator%num ==0:
		break

print denominator/num