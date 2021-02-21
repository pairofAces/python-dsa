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
        
        # at this point, if the element at the array's index is 
        # equal to the element at the sequence's index,
        # increment the sequence index
        if array[arrIdx] = sequence[seqIdx]:
            seqIdx += 1
        
        # after getting out of the 'if' logic and the sequence index
        # is successfully incremented, increment the array's index
        arrIdx += 1
    
    # after the while loop, return the boolean value of
    # seqInx is equal to the length of the sequence.
        # at this point the sequence index should be the same as 
        # the length of the sequence and therefore will be 'TRUE'
    return seqIdx == len(sequence) 