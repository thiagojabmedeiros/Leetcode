thiago = "thiago jose de almeida barroso medeiros"
l, r = 0, 0
res = ""

while r < len(thiago):
    if thiago[r] != " ":
        r += 1
    else:
        res += thiago[l:r+1][::-1]
        r += 1
        l = r
res += " "
res += thiago[l:r+1][::-1]
    
print(res[1:])