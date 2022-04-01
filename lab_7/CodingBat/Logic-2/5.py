def round_sum(a, b, c):
    return round10(a) + round10(b) +round10(c)

def round10(num):
    a = num % 10 
    if a >= 5:
        num += 10 - a
    else: num -= a
    return num