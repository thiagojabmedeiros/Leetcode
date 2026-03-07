
def longestsequence(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

numsx = [2,20,4,10,3,4,5]
print(longestsequence(numsx))

















# def longestConsecutiveSequence(nums):
#     num_set = set(nums)
#     sequence = 0

#     for i in num_set:
#         if (i - 1) not in num_set:
#             length = 1
#             current = i
#             while current + 1 in num_set:
#                 current += 1
#                 length += 1
#             sequence = max(sequence, length)
#     return sequence