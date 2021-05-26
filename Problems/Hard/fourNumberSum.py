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
                # create two variables
                    # one for the current sum, which would be the current element
                    # (i) in the array, plus the element (j) in the array
                current = array[i] + array[j]
                
                    # another for the difference between the targetSum and current
                difference = targetSum - current
                
                # use an id statement to check if the (difference) variable's value
                # is contained in (allSums) dictionary
                if difference in allSums:

                    # use a for loop, to traverse through each sum combination in
                    # the (allSums) dictionary, at the index of (difference)
                    for sum in allSums[difference]:
                        # append the (sum) and an array of the (i)th element and (j)th
                        # element in the input array
                            # this will create a 2-dimensional array
                        quadruplets.append(sum + [array[i], array[j]])
            
            # initiate a second for loop
            for k in range(o ,i):
                # create a variable to represent the current sum
                current = array[i] + array[k]

                # use an if statement, to check if the (current) sum is not contained in
                # (allSums)
                if current not in allSums:
                    