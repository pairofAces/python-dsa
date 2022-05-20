from collections import defaultdict
from typing import List

# Given an array of strings (strs), group the anagrams together. You can
# return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Time Complexity: 
    # O(m * n), where (m) is the length of the array of strings
    # and (n) is the length of each string in the array of strings

def groupAnagrams(strs: List[str]):
    # mapping character count to the list of anagrams
        # Key:Value -> charCount : list of anagrams
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26 # an array of 0s for each letter in the alphabet 

        for c in s:
            count[ord(c) - ord("a")] += 1

        # since lists cannot be keys in python, we can change the (count)
        # array into a tuple, b/c tuple's are not mutable
        res[tuple(count)].append(s)

    # only need to return the values, which are the anagrams grouped together
    return res.values()

array = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(array))