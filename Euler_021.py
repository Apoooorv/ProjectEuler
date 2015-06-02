import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

def calculateSum(n):
    numberlist = list(divisorGenerator(n))
    sum = 0
    for i in range(numberlist.__len__()-1):
        sum+= numberlist[i]
    return sum

sum = 0
for i in range(1,10001):
    number = calculateSum(i)
    if calculateSum(number) == i and i!=number:
        sum += i
                
print sum