def collatz_length(x):
    steps = 0
    while x != 1:
        steps += 1
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1

    return steps

max_steps = 0
longest_sequence_number = 0

for x in xrange(2,1000000):
    
    steps = collatz_length(x)
    if steps > max_steps:
        max_steps = steps
        longest_sequence_number = x

    if x % 10000 == 0:
        print x
        print steps

print longest_sequence_number





