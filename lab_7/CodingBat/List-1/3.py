def reverse3(nums):
    nums_2 = []
    for j in range(len(nums)):
        nums_2.append(nums[len(nums) - 1 - j])
    return nums_2
