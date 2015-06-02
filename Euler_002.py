a = 1
b = 2
result = 0

while b < 4000000:
    result = result + b
    a,b = b,b+a
    a,b = b,b+a
    a,b = b,b+a

print result