# Single Cycle Check

# Given an array of integers, where each integer represents
# a jump of its value. For instance, an integer of 2 represents a jump
# of 2 forward in the array. An integer of -3 represents a jump of 3 backwards
# in the array. 

# if a jump spills past an arrays bounds, it wraps to the other side. For example,
# a jump of -1 at index (0) will bring you to the last index in the array. A jump
# of 1 at the last index of the array will bring you to index (0).

# Create a function that will return a boolean representing if the jumps in the 
# array form a single cycle. 
    # NOTE: A single cycle is when, starting at any index and following the jumps,
    # every element in the array is visited exactly once before landing on the 
    # starting index

def hasSingleCycle(array):
    