# Two Number Sum

# given a non-empty array of distinct integers and an 
# integer representing a target sum
    # if any 2 numbers add up to the target integer
        # return the 2 numbers in an array
    # if no numbers add up to the target
        # return an empty array

# Solution 1
# O(n^2) time | O(1) space -> b/c storing info in just 2 variables
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# Solution 2
# O(n) time | O(n) space -> b/c using a hash table
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# Solution 3 ->sorting the array initially
# O(nlog(n)) time -> using the sorting method 
# O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []