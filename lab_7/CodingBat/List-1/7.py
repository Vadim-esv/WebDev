def max_end3(nums):
    a = max(nums[0], nums[len(nums) - 1])
    b = len(nums) 
    nums = [a for i in range(b)]
    return nums