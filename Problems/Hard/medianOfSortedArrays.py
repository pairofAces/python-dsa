# leetcode 4, median of two sorted arrays

# prompt

# given two sorted arrays (nums1) and (nums2) of size (m) and (n)
# respectively, return the median of the two sorted arrays

# the run time complexity should be O(log (m + n))

class Solution:
    def findMedianSortedArray(self, nums1: List[int], nums2: List[int]) -> float:
        # initate variables to hold the input arrays2
        A, B = nums1, nums2 

        # create variables to hold total and half integers
        total = len(nums1) + len(nums2)
        half = total // 2

        # initate if statement 
        if len(B) < len(A):
            # switch the variables values
            A, B = B, A
        
        1, r = 0, len(A) - 1

        # initiate while loop
        while True:
            i = (1 + r) // 2 #A
            j = half - i - 2 #B