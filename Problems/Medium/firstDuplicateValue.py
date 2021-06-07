# First Duplicate Value

# Prompt

# Given an array of integers between 1 and n, inclusive, where n is the
# length of the array, create a function that returns the first integer
# that appears more than once. 
    # note, only when the array is read from left to right
    # if no integer is repeated, return a -1
    # the input array can be mutated

# SOLUTION 1

# Complexity Analysis
    # Time: O(n^2) time, where (n) is the length of the input array

    # Space: O(1) space

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

# SOLUTION 2

# Complexity Analysis
    # Time: O(n) time, where (n) is the length of the input array

    # Space: O(n) space, where (n) is the length of the set that was created
    
class Solution2:
    def firstDuplicate(array):
        # create a empty dictionary
        checked = set()

        # initiate a for loop to traverse the input array
        for val in array:
            # if the element is in (checked)
            if val in checked:
                # return the value
                return val
            
            # if not, then add the element into the dictionary initially created
            checked.add(val)
        
        # if the duplicate isn't found (or if there weren't any)
        # return a -1, as requested by the problem
        return -1

# Solution 3

class Solution3:
    def firstDuplicate3(array):
        # initiate for loop to traverse every element in the input array
        for value in array:
            # reference the absolute value of the current value
            absoluteValue = abs(value)
            
            # initiate if statement, if the element at the index of 
            # the (absoluteValue) variable minus 1, is a negative
            if array[absoluteValue - 1] < 0:
                # then return the (absoluteValue) variable
                return absoluteValue
            
            # make the element at the index of (absoluteValue) minus 1,
            # a negative by multipying with (-1)
            array[absoluteValue - 1] *= -1
        
        # if no duplicate was found, return a (-1)
        return -1
