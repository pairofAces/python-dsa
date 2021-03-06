# SMALLEST DIFFERENCE
# Prompt

# create a function that takes two parameters, 2 non-empty
# arrays of integers. The function will find the pair of numbers,
# whos absolute difference is closest to 0.
    # return the array containing these two numbers
    # first number should be from first array and second
    # number should be from the second array
def smallestDifference(arrayOne, arrayTwo):
    # sort both arrays
    arrayOne.sort()
    arrayTwo.sort()

    # create the variables
    idxOne = 0
    idxTwo = 0
    smallest = Float("inf")
    current = Float("inf")
    smallestPair = []

    # use a while loop for when the idx variables ar less than the 
    # respected array lengths
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        # create variables for the 1st and 2nd numbers
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        # use an if statement to compare the firstNum and secondNum
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    
     