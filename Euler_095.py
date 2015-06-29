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

def chain(n):
    number = n
    numberlist = []
    for i in xrange(50):
        number = calculateSum(number)
        numberlist.append(number)
        if number > 1000000:
            print number
            return []
        if number == n:
            return numberlist
        numberlist.append(number)
    return []

longest = 0
answer = []
number = 0
for i in xrange(2000000):
    chainindex = chain(i)

    if len(chainindex) > longest:
        longest = len(chainindex)
        answer = chainindex

answer.sort()
print answer[0]