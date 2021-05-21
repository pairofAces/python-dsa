# KADANES ALGORITHM

# PROMPT

# Create a function that takes a non-empty array of integers and returns
# the maximum sum that can be obtained by summing up all of the integers 
# in a non-empty subarray of the input array.

# A subarray must only contain numbers that are adjacent to each other
# in the input array

class Solution:
    def kadanesAlgorithm(array):
        # create two variables to represent the current max and 
        # the ending location of the max
        maxEnding = array[0]
        currentMax = array[0]

        # initiate a for loop
        for i in range(1, len(array)):
            # create a variable to represent the (i)th element in the array
            num = array[i]

            # update the initial two variables
            maxEnding = max(num, maxEnding + num)
            currentMax = max(currentMax, maxEnding)