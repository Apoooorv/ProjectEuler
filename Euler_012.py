def get_number_of_divisors(n):
    i = 2
    divisors = set([])
    while (i * i <= n):
        if (n % i == 0):
            divisors.add(i)
            divisors.add(n/i)
        i = i + 1  
    return len(divisors) 

x = 1;
t = 1;

while(True):
    a = get_number_of_divisors(t)
    if a >= 499:
        print "answer : " + str(t)
        break
    x += 1
    t += x




    
