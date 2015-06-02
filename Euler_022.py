import os

def calculateSum(string):
    sum = 0
    for i in range(string.__len__()):
        sum += (ord(string[i])-64)
    return sum

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(os.path.join(__location__,'Euler_022_data.txt'), 'r')

data = fp.read()
data = sorted(data.split(','))

sum = 0
for i in range(data.__len__()):
    sum += (calculateSum(data[i]) * (i+1))
    
print sum
    