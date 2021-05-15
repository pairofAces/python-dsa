# VALIDATE BST

# PROMPT

# create a function that takes in a Binary Search Tree, which may be 
# invalid, and returns a boolean value reqpresenting whether the BST is 
# valid.

# Note: A BST is valid if and only if, all of its nodes are valud BST nodes

# create the BST class

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Solution:
    def validateBst(tree):
        # create a helper function that will take in more paramters
            # aspirational code
        return bstHelper(tree, float('-inf'), float('inf'))

    # create the helper function below
        # function will take in 3 parameters:
            # the BST itself, a minimum value, and a maximum value
    def bstHelper(tree, min, max):
        # if there is no tree
        if tree is None:
            # return True
            return True

        # if the value of the tree is less than the minimum, 
        # or grater than the maximum
        