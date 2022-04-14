# Leetcode 217 - Contains Duplicate

# Given an integer array (nums), return true if any value appears at least
# twice in the array, and return false if every element is unique.

class Solution:
    def containsDuplicate(self, nums : List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

class Solution1:
    def containsDup(self, nums : List[int]) -> bool:
        return len(set(nums)) < len(nums)