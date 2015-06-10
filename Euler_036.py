import math

def is_palindrome(number):
    number = str(number)
    reversed_number = reversed(number)
    
    if list(number) == list(reversed_number):
        return 1
    return 0

sum = 0
for i in range(1000000):
    if is_palindrome(i):
        if is_palindrome(str(bin(i))[2:]):
            sum+=i

print sum
print is_palindrome(str(bin(5))[2:])