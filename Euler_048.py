import math

sum  = 0

for i in range(1001):
  
    num = 1
    for j in range(1,i+1):
    	num *= i
    sum+=num

print sum%10000000000
