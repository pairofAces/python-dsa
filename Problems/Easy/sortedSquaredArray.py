# Sorted Squared Array

# create a function that takes an array of integers,
# sorted in ascending order, and returns a new array
# of the same length, with the squares of the original integers
# also in ascending order

# SOLUTION 1

    # Complexity
        # Time: O(n logn) time, where (n) is the length of the input array
        # Space: O(n) space,  where (n) is the length of the array created
    
def sortedSquaredArrays(array):
    # create a new array filled with 0's, 
    # for the same length as the input array
    sortedSquares = [0 for _ in array]

    # initiate a for loop to traverse through the input array
    for i in range(len(array)):
        # create a variable to represent the i'th element
        # in the array
        currValue = array[i]

        # insert the square of the current value, into the
        # new array we created at the i'th index
        sortedSquares[i] = currValue * currValue
    
    # sort the sortedSquares array
    sortedSquares.sort()

    # return the final sortedSquares array
    return sortedSquares


# SOLUTION 2 - OPTIMAL - not using built-in sort method

    # Complexity Analysis
        # Time: O(n) time, where (n) is the length of the input array
        # Space: O(n) space, where (n) is the lengt of the created array
        
def sortedSquaredArrays(array):
    # create an array of the same length
    sortedSquares = [0 for _ in array]

    # create index pointers for the positions of the smallest 
    # and largest values
    smallerIndex = 0
    largerIndex = len(array) - 1

    # initiate a for loop starting from the ending of the
    # input array -> using the reversed method
    for i in reversed(range(len(array))):
        # create variables to represent the smaller value and 
        # larger value
        smallerValue = array[smallerIndex]
        largerValue = array[largerIndex]

        # use an if/else statement
            # if the absolute value of the smaller value
            # is greater than the absolute value of the 
            # larger value, then the element at the i'th
            # position will be set to the square of the 
            # smaller value && the index will be incremented

            # else, the element in the i'th position of
            # the created array will be set to the square
            # of the larger element, and the index will be
            # decremented

            if abs(smallerValue) > abs(largerValue):
                sortedSquares[i] = smallerValue * smallerValue
                smallerIndex += 1
            else:
                sortedSquares[i] = largerValue * largerValue
                largerIndex -= 1

            # finally, return the sortedSquares array
            return sortedSquares 