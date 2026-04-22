def productExceptSelf(nums):
    nNums = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        nNums[i] *= prefix
        prefix *= nums[i]

    postfix = nums[-1]
    for i in range(len(nums) - 2, - 1 , - 1):
        nNums[i] *= postfix
        postfix *= nums[i]
    print(nNums)

productExceptSelf([1,2,4,6])