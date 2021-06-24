# Maximum Depth of Binary Tree - Leetcode

# Given the root of a binary tree, return its maximum depth.

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if the root is empty
        if not root:
            # return a 0
            return 0
        
        # if the root is not empty
            # recursive call on both children nodes
        return (1 + max(self.maxDepth(self.left), self.maxDepth(self.right)))