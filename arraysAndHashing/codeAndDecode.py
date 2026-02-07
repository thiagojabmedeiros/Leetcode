def encode(strs):
    sizes = []
    res = ""

    for s in strs: # lets get the size of each string in the array
        sizes.append(len(s))
    print(sizes)

    for sz in sizes: # lets concaten the sizes in res and separate it by comma
        res += str(sz)
        res += ","
    res += "#" # separating the strings sizes to the strings by '#'
    print(res)

    for strings in strs: # catching the strings and joining them
        res += strings
    print(res)

    return res
    
def decode(s):
    size, res, i = [], [], 0 

    while s[i] != "#": # if it is still not "#" keep going through and reading
        if s[i] != ",": # if the character is not "," 
            size.append(int(s[i])) # add it in the array as an integer
        i += 1 # plus 1 every moment you are reading an element to see the next one

    i += 1 # here we have to sum 1 because i has "#" index saved 
    # now as we want to read next part of the string, the strings, we must plus one

    for sz in size: # reading the sizes in the size list
        res.append(s[i:(i + sz)]) # here we append the elements in the array when it start in i and end in i + sz
        i += sz # here we sum because its we want to see next element
    return res

strList = ["banana","cat","barbecue","shoes","christmas","australia", "boat"]
ss = encode(strList)
print(decode(ss))