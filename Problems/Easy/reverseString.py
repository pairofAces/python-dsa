# Reverse String - LeetCode

# create a function that reverses a string.
# the input string is provided as an array of
# characters

# Note: Don't return anything, modify (s) in-place

# Complexity Analysis
    # Time: O(n) time, where (n) is the lenght of the list

    # Space: O(1) constant space, because no external data structures
    # are being used

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # use python built-in method
        s.reverse()