def groupAnagrams(strs):
    seen = {}
    for value in range(len(strs)):
        key = "".join(sorted(strs[value]))
        if key in seen:
            seen[key].append(strs[value])
        else:
            seen[key] = [strs[value]]
    print(list(seen.values()))

strsx = ["act","pots","tops","cat","stop","hat"]
groupAnagrams(strsx)