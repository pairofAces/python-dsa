# Two Number Sum

# given a non-empty array of distinct integers and an 
# integer representing a target sum
    # if any 2 numbers add up to the target integer
        # return the 2 numbers in an array
    # if no numbers add up to the target
        # return an empty array

# Solution 1
# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
