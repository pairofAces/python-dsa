# Leet code 242

# Given two strings, s and t, return true if (t) is an anagram of (s),
# return false if not
# ---------------------------------------------------------------------
# Solution 1:

# Time Complexity: O(s + t), where (s) & (t) are the lengths of the
# strings respectively

# Space Complexity: O(s + t), because of the use of 2 external data
# structures -> the 2 hashmaps that were created
 
def isAnagram(s:str, t:str):
    # first check if the two input strings are equal in length
    # if they're not, then (t) cannot be an anagram of (s)
    if len(s) != len(t):
        return False
    
    # create dictionary objects for both strings
        # keys : each letter in the strings
        # values: how many times each letter appeared
    countS, countT = {}, {}

    # iterate over the length of (s)
        # at this point, I know that the 2 strings are equal length
    for i in range(len(s)):
                        #    if I used countS[s[i]], the code will
                        #    throw a 'Key Error', if the key isn't
                        #    present in the hashmap. To get around this,
                        #    I can use the built-in .get method. 
                            # if the first input for .get method is in
                            # the hashmap, retrieve that value. Otherwise,
                            # set that key to a value of 0.
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    # iterate over the hashmaps, to check if the values of each 
    # Key:value pair are the same
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    
    return True

# ---------------------------------------------------------------------
# Solution 2

# What if I wanted to create a solution with a space complexity of
# O(1), constant space. Meaning no use of external data structures.

# If the two input strings are anagrams, that means if they are sorted
# they will be equal.  
    # python has a built in function that will allow me to check this
    # (sorted)

def checkAnagram(s: str, t: str) -> bool:
    print(sorted(s) == sorted(t))

s = "link"
t = "kinl"

# isAnagram(s, t)
checkAnagram(s, t)
