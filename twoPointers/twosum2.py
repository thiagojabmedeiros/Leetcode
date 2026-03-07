def twoSum2(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] > target:
            r -= 1
            continue
        else:
            l += 1
            continue
    return []

numbers = [1,2,3,4]
targetx = 3

print(twoSum2(numbers, targetx))
