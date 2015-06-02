import math

number = math.factorial(100)
number = str(number)

sum = 0
for i in range(0,number.__len__()):
    sum+=int(number[i])
    
print sum