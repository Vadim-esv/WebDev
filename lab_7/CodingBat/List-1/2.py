def common_end(a, b):
    if a[0] == b[0]:
        return True
    elif a[len(a) - 1] == b[len(b) - 1]:
        return True
    else: return False