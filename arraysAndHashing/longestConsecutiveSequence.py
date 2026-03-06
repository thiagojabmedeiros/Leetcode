
def longestsequence(nums):
    snums = set(nums)
    i = 0
    print(snums)
    while i < len(snums):
        print(snums)
        i+= 1
    print(i)

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