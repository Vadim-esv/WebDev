def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i != len(nums) - 1:
                nums[i+1] = 0
        sum += nums[i]
    return sum