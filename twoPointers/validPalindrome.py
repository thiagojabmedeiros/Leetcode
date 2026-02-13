def validPalindrome(s):
    symbolList = ["","°"," ",",", "!", "#", "$", "@", ";", "%", "¨", "&", "*", "(", ")", "-", "+", "-", "?", "'", ".", ":", ";", ">", "<", "/", "|", "=", "º"]
    for i in range(len(s)):
        if s[i] in symbolList:
            s = s.replace(s[i], "")
        s = s.lower()
    
    return s == s[::-1]
        

phrase = "aA"
print(validPalindrome(phrase))