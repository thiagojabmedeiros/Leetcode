def encode(strs):
    code = ""
    for string in strs:
        code += str(len(string)) + "#" + string
    return code

def decode(code):
    strs = []
    i = 0

    while i <= len(code) - 1:
        sz = ""
        while code[i] != "#":
            sz += code[i]
            i += 1
        i += 1
        j = int(sz) + i
        strs.append(code[i:j])
        i = j
    print(strs)
    
strs = ["banana", "apple", "avocado", "orange"]
code = encode(strs)
decode(code)