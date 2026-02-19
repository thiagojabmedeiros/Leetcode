def validPalindrome(s):
    s = s.upper()
    l, r = 0, len(s) - 1

    while l != r:
        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
    
    return True

        
phrase = "Was it a car or a cat I saw?"
print(validPalindrome(phrase))