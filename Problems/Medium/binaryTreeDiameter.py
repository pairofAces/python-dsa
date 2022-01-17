# Binary Tree Diameter

# create a function that takes in a Binary Tree and returns its 
# diameter. The diameter is the length of the longest path, even
# if the diameter doesn't pass through the root of the tree. 

class TreeHelper:
    def__init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

class BinaryTree:
    def__init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Complexity Analysis
    # Time: O(n) time, where (n) is the number of nodes in the Binary Tree

    # Space: O(h) space, where (h) is the height of the Binary Tree
    

class Solution:
    def binaryTreeDiameter(tree):
        # aspirational code
            # helper method to return the diameter 
        return getTreeInfo(tree).diameter

    def getTreeInfo(tree):
        if tree is None:
            # create a class to handle the tree information
            return TreeHelper(0, 0)
        
        # create variables to represent the left and right tree info
            # use recursion
        leftTreeInfo = getTreeInfo(tree.left)
        rightTreeInfo = getTreeInfo(tree.right)

        # create a variable to represent the longest path
        longestPathFromRoot = leftTreeInfo.height + rightTreeInfo.height

        # create a variable to represent the max diameter
        maxDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter)

        # make a reference to the current diameter
        currentDiameter = max(longestPathFromRoot, maxDiameter)

        # make a reference to the current height
        currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

        # return the TreeHelper class with the current diameter and height
        return TreeHelper(currentDiameter, currentHeight)