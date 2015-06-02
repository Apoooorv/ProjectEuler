def is_prime(n):
    i = 2
    factors = []
    while (i * i <= n):
        if (n % i == 0):
            return False
        i = i + 1   
    return True

n = 2
i = 0

while(True):
    if (is_prime(n)):
        if (i == 10002):
            print n
            break
        else:
            print n
            i += 1
    n += 1
