def array123(nums):
    a = False
    b = False
    c = False
    for i in nums:
        if i == 1:
            a = True
        if i == 2:
            b = True
        if i == 3:
            c = True
    if(a and b and c):
        return True
    else: return False