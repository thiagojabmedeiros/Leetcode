def longestConsecutiveSequence(nums):
    num_set = set(nums)
    sequence = 0

    for i in num_set:
        if (i - 1) not in num_set:
            length = 1
            current = i
            while current + 1 in num_set:
                current += 1
                length += 1
            sequence = max(sequence, length)
    return sequence


numsx = [0,3,2,5,4,6,1,1]
print(longestConsecutiveSequence(numsx))