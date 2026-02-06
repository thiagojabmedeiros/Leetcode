def containsDuplicate(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        else:
            seen[nums[i]] = i
    return False


test = [1, 2, 3, 4]
print(containsDuplicate(test))