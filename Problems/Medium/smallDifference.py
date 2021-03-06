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