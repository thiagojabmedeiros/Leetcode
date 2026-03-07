def groupAnagrams(strs):
    seen = {}
    res = []
    for word in strs:
        key = "".join(sorted(word))
        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]
    for arr in seen.values():
        res.append(arr)
    return res

strsx = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strsx))