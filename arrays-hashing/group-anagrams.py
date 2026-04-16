def groupAnagrams(strs):
    seen = {}
    for s in strs:
        ss = "".join(sorted(s))
        if ss in seen:
            seen[ss].append(s)
        else:
            seen[ss] = [s]

    strs2 = []
    for v in seen.values():
        strs2.append(v)
    
    print(strs2)

strs = ["act","pots","tops","cat","stop","hat"]
groupAnagrams(strs)