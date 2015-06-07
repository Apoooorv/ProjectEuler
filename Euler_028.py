def convert(flag):
	if flag:
		return 1
	return -1

number = 0
parent = []
gridRange = 1001
for i in range(gridRange):
	child = []
	for j in range(gridRange):
		child.append(number)
	parent.append(child)

row = gridRange/2
col = gridRange/2
number = 1
flag = False
stopflag = False

parent[row][col] = 1

for i in range(1,gridRange):
	for j in range(1,i+1):
		col += (-1)*convert(flag)
		number += 1
		parent[row][col] = number

	for j in range(i):
		row += (-1)*convert(flag)
		number+=1
		parent[row][col] = number
	flag = not flag

for i in range(col,gridRange):
	col += 1
	if col == gridRange:
		break
	number += 1
	parent[row][col] = number	

# for i in range(gridRange):
# 	print parent[i]

sum = 0
for i in range(gridRange):
	sum += parent[i][i]
	sum += parent[i][gridRange-1-i]

print sum-1