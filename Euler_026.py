from __future__ import division

def division(numerator,denomerator):
	decimal_found = False

	v = numerator//denomerator
	numerator = 10*(numerator - v*denomerator)
	answer = str(v)

	if numerator == 0:
		return answer

	answer += '.'

	states = {}

	while numerator > 0 :
		prev_state = states.get(numerator,None)
		if prev_state!=None:
			start_repeat_index = prev_state
			non_repeating = answer[:start_repeat_index]
			repeating = answer[start_repeat_index:]
			return non_repeating + '[' + repeating + ']'

		states[numerator] = len(answer)

		v = numerator // denomerator
		answer+= str(v)
		numerator -= v*denomerator
		numerator *= 10

	if numerator > 0:
		return answer + '...'
	return answer

greatest = 0
greatestNumber = 1
for i in xrange(1,1000):
	number = division(1,i)
	start = number.find('[')
	end = number.find(']')
	answer = end-start
	if answer > greatest:
		greatest = answer
		greatestNumber = i

print greatestNumber