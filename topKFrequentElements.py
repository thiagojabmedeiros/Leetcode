def topKFrequentElements(nums, k):
    count = {}
    for key in nums:
        count[key] = count.get(key, 0) + 1
    
    freq = []
    for key, value in count.items():
        freq.append([value, key])
    freq.sort()

    res = []
    while len(res) < k:
        res.append(freq.pop()[1])
    return res


numsx = [10,55,55,22,22,22]
print(topKFrequentElements(numsx, 2))
