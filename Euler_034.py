import math

grandsum = 0
for i in range(3,1000000):
    sum = 0
    string = str(i)
    for digit in string:
        sum+=math.factorial(int(digit))
    if sum == i:
        print i
        grandsum+=i
        
print grandsum        