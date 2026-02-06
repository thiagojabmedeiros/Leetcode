def validAnagram(s, t):
    x = sorted(s)
    y = sorted(t)

    return x == y

ss = "thiago"
tt = "ogthai"
print(validAnagram(ss,tt))