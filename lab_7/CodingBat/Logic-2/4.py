def lone_sum(a, b, c):
    if a == b == c:
        a = 0
        b = 0
        c = 0
    elif a == b:
        a = 0 
        b = 0
    elif a == c:
        a = 0
        c = 0
    elif b == c:
        b = 0
        c = 0
    return a + b + c