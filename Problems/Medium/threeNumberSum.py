# Three Number Sum

# Prompt:
# create a function that takes in a non-empty array of distinct integers
# and a target sum.
    # function should find all triplets in the array that add up to the 
    # target integer
        # the triplets need to be returned in an array
# if no triplets are found, return and empty array


# Solution
# Time Complexity: O(n^2) time
# Space Complexity: O(n) space
def threeNumberSum(array, targetSum):
    # first sort the array
    array.sort()
    # create the empty array in a var
    triplets = []
    # use a for loop to traverse the original array
    for i in range(len(array - 2)):
        # create two pointer variables
        left = i + 1
        right = len(array) - 1
        # use a while loop to activate when the left < right
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            # use 'if' logic to check is currentSum = targetSum
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    # finally, return the triplets array
    return triplets