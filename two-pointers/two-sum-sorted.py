def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            print([l + 1, r + 1])
            return True
    return False

nums = [1,3,5,6,9,12]
twoSum(nums, 11)