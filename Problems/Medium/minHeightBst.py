# Min Height Bst

# create a function that takes in a non-empty sorted array of distinct integers
# constructs a BST from the integers, and returns the root of the BST.

# The function should minimize the height of the BST.

class Solution:
    def minHeightBst(array):
        # implement a helper function
            # following paramerers:
                #  array, BST, starting Index, and the ending index
        minHelper(array, None, 0, len(array) - 1)

    # create helper function here
    def minHelper(array, bst, startIdx, endingIdx):
        # if the startIdx is less than the endingIdx
        if startIdx < endingIdx:
            return 

        # return the midpoint of the index values and get the element in that index
        midpoint = (startIdx + endingIdx) // 2
        elementFound = array[midpoint]

        # if the BST is none, create a BST with the value of the elementFound
        if bst is None:
            bst = BST(elementFound)
        
        # else, if there is a value for the BST, insert the elementFound variable
        # as a new node on the BST
        else:
            bst.insert(elementFound)
        
        # use recursion to implement the helper method,
        # with the array, bst, and then using the following
        # as the final 2/4 parameters
            # one -> starting index, mid point - 1
            # two -> mid point + 1, ending index
        minHelper(array, bst, startIdx, midpoint - 1)
        minHelper(array, bst, midpoint + 1, endingIdx)
            
        

class BST:
    def__init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)