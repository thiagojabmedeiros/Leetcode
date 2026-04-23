def longestConsecutiveSequence(nums):
    sNums = set(nums)
    maxC = 0
    count = 0
    for n in sNums:
        if n - 1 not in sNums:
            current = n
            count = 1
            while current + 1 in sNums:
                current += 1
                count += 1
            maxC = max(maxC, count)

    print(maxC)


nums = [0,3,2,5,4,6,1,1]

longestConsecutiveSequence(nums)