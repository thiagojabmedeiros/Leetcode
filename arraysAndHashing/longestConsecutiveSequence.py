def longestConsecutiveSequence(nums):
    seen = {}
    sequence = 0
    for i in range(len(nums)):
        seen[nums[i]] = seen.get(nums[i], 0) + 1
        
    for i in range(len(nums)):
        if (nums[i] + 1) in seen:
            sequence += 1
        elif seen != {}:
            sequence = 1
        

    print(seen)
 

numsx = [0,3,2,5,4,6,1,1]
longestConsecutiveSequence(numsx)