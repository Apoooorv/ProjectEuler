import math

def is_abundant(number):
    i = 1
    sum = 0
    j = number
    while True:
        if number % i == 0:
            div = number/i
            if i!=div:
                sum += i
            sum+=div
            j = div
        i+=1
        if i>=j:
            break
    
    sum-=number
    if sum>number:
        return 1
    return 0
    
abundantlist = []

for i in xrange(1,28124):
    if is_abundant(i):
        abundantlist.append(i)

abundantsumlist = []
for i in xrange(abundantlist.__len__()):
    for j in xrange(i,abundantlist.__len__()):
        abundantsumlist.append(abundantlist[i] + abundantlist[j])

sum = 0
for i in xrange(28124):
    if i in abundantsumlist:
        pass
    else:
        sum+=i

print sum