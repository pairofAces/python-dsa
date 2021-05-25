# FOUR NUMBER SUM

# PROMPT

# Create a function tha takes in a non-empty array of unique integers and an
# integer that represents a target sum. 

# The function should find all quadruplets in the array that sum up to the 
# target sum, and return a two-dimensional array of all these quadruplets.

# Note, order doesn't matter. 

# If there aren't any quadruplets, the function should return an empty array. 

class Solution:

    def fourNumberSum(array, targetSum):
        # create a dictionary for all the combinations of sums
        allSums = {}

        # create an array variable to represent the final array
        # containing all the quadruplets
        quadruplets = []

        # initiate a for loop
        for i in range(1, len(array) - 1):
            # a nested for loop
            for j in range(i + 1, len(array)):
                