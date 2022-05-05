# Leet code 242

# Given two strings, s and t, return true if (t) is an anagram of (s),
# return false if not

def isAnagram(self, s:str, t:str):
    # first check if the two input strings are equal in length
    # if they're not, then (t) cannot be an anagram of (s)
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    
    return True
