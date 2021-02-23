# Three Number Sum

# Prompt:
# create a function that takes in a non-empty array of distinct integers
# and a target sum.
    # function should find all triplets in the array that add up to the 
    # target integer
        # the triplets need to be returned in an array
# if no triplets are found, return and empty array

def threeNumberSum(array, targetSum):
    # first sort the array
    array.sort()
