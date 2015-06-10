import math

def is_abundant(number):
    i = 2
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
    
    sum+=1
    if sum>number:
        return 1
    return 0

def sum_abundant(number):
    if number < 12:
        return 1
    i = 12
    j = number-i
    while j>=i:
        if is_abundant(i) and is_abundant(j):
            return 1
        i+=1
        j-=1
    return 0

sum = 0
print sum_abundant(20161)
# for i in range(28524):
#     if not sum_abundant(i):
#         print i
#         sum+=i
#         
# print sum