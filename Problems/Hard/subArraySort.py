# Subarray Sort

# The prompt

# create a function that takes an array of at least 2 integers
# and returns an array of the starting and ending indices of the smallest
# subarray in the input array that needs to be sorted in place, in order
# for the entire input array to be sorted, in ascending order. 
    # Note - if the input array is already sorted then return 
    #        [-1, -1]

class Solution:
    def subarraySort(array):
        # create 2 variables, one for minimum and maximum
        minNum = float('inf'')
        maxNum = float('-inf')

        # use a for loop relative to the aray's length
        for i in range(len(array)):
            # create a variable to be equal to the (i)th element in 
            num = array[i]

            # use an if statement, aspirational code -> helper function
            if outOfOrder(i, num, array):

# create helper function below
def outOfOrder(i, num, array):