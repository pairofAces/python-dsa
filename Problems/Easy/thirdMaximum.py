# Third Maximum Number - LeetCode 414

# Given an integer array, nums, return the third maximum number in the
# input array. 
    # If the third maximum doesn't exist, return the maximum


# Complexity Analysis
    # Time: O(n) time, where (n) is the length of the input array

    # Space: O(1) space, since no external data structures were used
    
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # initiate comparison variables
        max = None
        second_Max = None
        third_Max = None

        # initiate for loop to traverse through the (nums) array
        for num in nums:
            # edge cases where the next element is the same as the element
            # before
            if num == max or num == second_Max or num == third_Max:
                # move on
                continue

            # if/else statements
            # if the max, second_Max, third_Max, are None or less than the
            # current (num)
            if max == None or num > max:
                third_Max = second_Max
                second_Max = max
                max = num
            elif second_Max == None or num > second_Max:
                third_Max = second_Max
                second_Max = num
            elif third_Max == None or num > third_Max:
                third_Max = num
            
        # edge case, when the third_Max is None at this point
        if third_Max == None:
            # then return the maximum
            return max
        
        # once the loops end, return the third_max
        return third_Max