def topKFrequent(nums, k):
    seen = {}
    for n in nums:
        seen[n] = seen.get(n, 0) + 1

    freq = []
    for key, value in seen.items():
        freq.append([value, key])
    freq.sort()
    freq = freq[-k:]

    res = []
    for i in range(len(freq)):
        res.append(freq[i][1])
    
    return res
    
nums = [1,2,2,3,3,3,4,5,5,6]
topKFrequent(nums, 2)