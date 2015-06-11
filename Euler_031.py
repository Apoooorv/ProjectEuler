count = 0
for h in xrange(3):
	for f in xrange(5):
		for t in xrange(11):
			for u in xrange(21):
				for g in xrange(41):
					for v in xrange(101):
						for o in xrange(201):
							if 100*h + 50*f + 20*t + 10*u + 5*g + 2*v + o == 200:
								# print str(h) + ',' + str(f) + ',' + str(t) + ',' + str(u) + ',' + str(g) + ',' + str(v) + ',' + str(o) + ','
								count += 1

print count+1