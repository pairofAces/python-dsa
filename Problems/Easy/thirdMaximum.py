# Third Maximum Number - LeetCode 414

# Given an integer array, nums, return the third maximum number in the
# input array. 
    # If the third maximum doesn't exist, return the maximum

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # initiate comparison variables
        max = None
        second_Max = None
        third_Max = None

        # initiate for loop to traverse through the (nums) array
        for num in nums:
            