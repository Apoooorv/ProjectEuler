def triangles(sum):
	count = 0
	triangleslist = []
	for hyp in xrange(1,sum):
		for i in xrange(1, sum/2):
			for j in xrange(i,sum/2):
				if i + j > hyp and i+j+hyp == sum:
					if (i*i) + (j*j) == (hyp)*(hyp):
						count += 1
	return count

greatest = 0
for sum in xrange(3,1001):
	count = triangles(sum)
	if greatest < count:
		greatest = count
		number = sum

print greatest
print sum