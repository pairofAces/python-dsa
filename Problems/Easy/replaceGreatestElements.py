from typing import List
# Leetcode 1299

# Replace Elements With Greatest Element on Right side

# given an array, arr, replace every element in the array with the
# greatest element among the elements to its right, and replace the last 
# element with -1.
# Then return the array

# example:
    # input array: [17, 18, 5, 4, 6, 1]
    # output: [18, 6, 6, 6, 1, -1]


class Solution:
    def replaceElem(self, arr:List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr