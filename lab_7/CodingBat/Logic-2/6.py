def lucky_sum(a, b, c):
    if b == 13:
        b = 0
        c = 0
    if c == 13:
        c = 0
    if a == 13:
        b = 0 
        a = 0
        c = 0
    return a + b + c
