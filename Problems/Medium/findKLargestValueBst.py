# Find Kth Largest Value in BST

# Create a function that takes a Binary Search Tree and an integer, k,
# that finds the (k)th largest integer in the BST. 

class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
class Solution:
    def findKthLargestValueInBst(tree, k):
        # create variable to represent array
        sortedNodeValues = []

        # aspirational code, helper method
        inOrderTraverse(tree, sortedNodeValues)

        # return the element in the (sortedNodeValues) array, at the index
        # of the length of the array minus (k)
        return sortedNodeValues[len(sortedNodeValues) - k]
    
    def inOrderTraverse(node, sortedNodeValues):
        