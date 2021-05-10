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
                minNum = min(minNum, num)
                maxNum = max(maxNum, num)
        
        # use an if statement to check if (minNum) will be equal to infinity
        if minNum == float('inf'):
            # then return an array of -1 and 1
            return [-1, 1]
        
        # create a variable set to 0, acting as an index pointer
        leftIdx = 0

        # while the minNum is greater than or equal to the element at the
        # index of (leftIdx)
        while minNum >= array[leftIdx]:
            # increment the leftIdx
            leftIdx += 1
        
        # now create another variable to represent the index, starting from
        # right-end of the array
        rightIdx = len(array) - 1
        


# create helper function below
def outOfOrder(i, num, array):