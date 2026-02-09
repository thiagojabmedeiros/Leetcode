def longestCommonPrefix(strs):
    seen = {}
    for i in strs:
        prefix = ""
        for x in i:
            prefix += x
            seen[prefix] = seen.get(prefix, 0) + 1
    
    res = []
    for k, v in seen.items():
        if v == len(strs):
            res.append([v, k])
    res.sort()
    print(res[-1][1])

names = ["best", "bester", "boter", "bant", "black"]
print(longestCommonPrefix(names))
