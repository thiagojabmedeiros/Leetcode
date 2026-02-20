def threeSum(nums):
    seenSum = {}
    l, r = 0, 0
    max = 1
    while l < len(nums):
        r += 1

        sum = nums[l] # sum is gonna receive the element in nums[l] 
        sum += nums[r] # then it sums  with the next nums[r]
        max += 1 # here we count how many numbers has in the sum

        if max == 3: # if it has 3 elements in the sum
            l += 1
            r = l


numsx = [-1,0,1,2,-1,-4]
threeSum(numsx)