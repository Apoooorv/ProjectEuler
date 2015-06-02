for a in range(999,80,-1):
    for b in range(999,80,-1):
        if str(a*b) == str(a*b)[::-1]:
            print a*b
            break
