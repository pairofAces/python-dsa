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
            # create a variable to represent the (i)th element in the array
            current = array[i]

            # initiate another for loop to start at 1 position higher than (i)
            for j in range(i + 1, len(array)):
                # create another variable to represent the (j)th element in the array
                compare = array[j]

                # initate an if statement to compare (current) to (compare)
                if current == compare:
                    # if it is, then set (minimumIndex) to the minimum between 
                    # it's current value and (j)
                    minimumIndex = min(minimumIndex, j)
        
        # edge case
            # if the minimumIndex is equal to the length of (array)
        if minimumIndex == len(array):
            return -1
        
        # after getting out of the previous loops,
        # return the element in the array, at the index of (minimumIndex)
        return array[minimumIndex]