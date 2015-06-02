factors = []

def get_prime_factors(n):
    i = 2
    factors = []
    while (i * i <= n):
        while (n % i == 0):
            n = n / i
            factors.append(i)
        i = i + 1   
    if (n != 1):
        factors.append(n)
    return factors

for i in range(2,20):
    print 2*2*2*2*3*3*5*7*11*13*17*19

def check_if_prime(n):
    i = 2
    factors = []
    while (i * i <= n):
        while (n % i == 0):
            return false
        i = i + 1   
    return true