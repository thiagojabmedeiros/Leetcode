def topKFrequentElements(nums, k):
    seen = {}
    freq, res = [], []
    for key in nums:
        seen[key] = seen.get(key, 0) + 1
    for key, value in seen.items():
        freq.append([value, key])
    freq.sort()
    for i in freq[-k:]:
        res.append(i[1])
    return res

numsx = [10,55,55,22,22,22,33,33,33]
print(topKFrequentElements(numsx, 1))
