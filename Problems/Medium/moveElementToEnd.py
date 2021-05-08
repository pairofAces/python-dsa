# MOVE ELEMENT TO END

# PROMPT

# Given an array of integers and an integer, create a function that moves
# all instances of that integer in the array to the end of the array and 
# returns the array.

# Note -> function should mutute the input array, the order of the other
# integers in the array don't need to be maintained

# Complexity:
    # Time: O(n) time, where (n) is the length of the input array
    # Space: O(1) space, constant space
class Solution:
    def moveElementToEnd(array, toMove):
        # create two pointer variables
        i = 0
        j = len(array) - 1

        # use a while loop to initiate as long as (i) is less than
        # (j)
        while i < j:
            # initiate a nested while loop to make sure (i) is still
            # less than (j) and the (j)th element in the array is equal
            # to the integer value of (toMove)
            while i < j and array[j] == toMove:
                # if the conditions are met, decrement (j)
                j -= 1
            
            # initiate an if statement, for when the (i)th element in
            # the array is equal to (toMove)
            if array[i] == toMove:
                # if so, set the (i)th element in the array to be the 
                # (j)th element, and set the (j)th element to be equal to
                # the (i)th element
                array[i], array[j] = array[j], array[i]
            
            # after getting out of the if statement, increment (i) by 1
        
        # after the inital while loop is complete, return the final array
        return array