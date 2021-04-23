# Sorted Squared Array

# create a function that takes an array of integers,
# sorted in ascending order, and returns a new array
# of the same length, with the squares of the original integers
# also in ascending order


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
