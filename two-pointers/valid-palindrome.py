def validPalindrome(s):
    l, r = 0, len(s) - 1
    x = [",", ".", ";", ":", "?", "!", "'", " "]
    while l < r:
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
            continue
        if s[l] in x:
            l += 1
            continue
        if s[r] in x:
            r -= 1
            continue
        else:
            return False
    return True
        
s = "Was it a car or a cat I saw?"
print(validPalindrome(s))