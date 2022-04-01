def sum2(nums):
    sum = 0
    i = 0
    while(i in range(len(nums)) and i < 2):
        sum += nums[i]
        i += 1
    return sum