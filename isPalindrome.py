def toLower(s):
    lowers = ""
    for c in s:
        c = c.lower()
        lowers += c
    return lowers


# print(toLower("GFgggftYBXjiIIOlh"))

def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


print(isPalindrome("qwerytrewq"))