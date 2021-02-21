# Validate Subsequence

# Prompt:
    # Given two non-empty array of integers, create a function that 
    # determines whether the second array is a subsequence of the 
    # first one.

# Subsequence: a set of numbers that don't have to be adjacent in
# the array but that are in the same order as they appear in the 
# initial array.

def isValidSubsequence(array, sequence):
    # create index variables for array and the sequence
    arrIdx = 0
    seqIdx = 0
    
    # create a while loop for when the array's index is less than
    # the array's length AND the same for the sequence index and length
    while arrIdx < len(array) and seqIdx < len(sequence):