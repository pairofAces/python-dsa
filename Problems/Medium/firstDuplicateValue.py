# First Duplicate Value

# Prompt

# Given an array of integers between 1 and n, inclusive, where n is the
# length of the array, create a function that returns the first integer
# that appears more than once. 
    # note, only when the array is read from left to right
    # if no integer is repeated, return a -1
    # the input array can be mutated

class Solution:
    def findDuplicateValue(array):
        # create a variable to represent the index we'll use as a comparison
        minimumIndex = len(array)

        # initiate a for loop to traverse the input array
        for i in range(len(array)):
            