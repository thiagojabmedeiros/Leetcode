def twoSum(nums, target):
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [i, seen[comp]]
            else:
                seen[nums[i]] = i

nums = [3,4,5,6]
target = 7
print(twoSum(nums, target))