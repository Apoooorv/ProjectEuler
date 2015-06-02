def is_prime(n):
    i = 2
    factors = []
    while (i * i <= n):
        if (n % i == 0):
            return False
        i = i + 1   
    return True

result = 0

for i in xrange (0,10):
    if (i%1000 == 0):
        print i
    if is_prime(i):
        result += i

print result