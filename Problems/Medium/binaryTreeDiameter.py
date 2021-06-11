# Binary Tree Diameter

# create a function that takes in a Binary Tree and returns its 
# diameter. The diameter is the length of the longest path, even
# if the diameter doesn't pass through the root of the tree. 

class BinaryTree:
    def__init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
class Solution:
    def binaryTreeDiameter(tree):