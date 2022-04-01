def make_bricks(small, big, goal):
    big_count = 0
    a = 0
    if goal < 5 and small >= 4:
        return True
    if goal < 5 and small < 4:
        return False
    while(goal > 5):
        goal %= 5
        big_count += 1
    if big_count <= big and goal == 0:
        return True
    elif big_count <= big and goal != 0:
        if goal <= small:
            return True
        elif goal > small:
            return False 
    if big_count > big:
        a = big_count * 5
        a = a + goal
        print(a)
        if small >= a:
            return True
        if small < a:
            return False
