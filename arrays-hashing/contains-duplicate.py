def hasDuplicate(nums):
    setNums = set(nums)
    return len(nums) == len(setNums)

nums = [1,2,3,3,4,5]
print(hasDuplicate(nums))