def twoSum(nums, target):
    seen = {}
    result = []
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in seen:
            result.append(seen[comp])
            result.append(i)
            return result
        else:
            seen[nums[i]] = i
    return None


listNums = [1,2,3,4,5,6,7,8,9,10]
print(twoSum(listNums, 10))