# Min Height Bst

# create a function that takes in a non-empty sorted array of distinct integers
# constructs a BST from the integers, and returns the root of the BST.

# The function should minimize the height of the BST.

class Solution:
    def minHeightBst(array):
        # implement a helper function
            # following paramerers:
                #  array, None, 0, and the length of th array
        minHelper(array, None, 0, len(array) - 1)

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