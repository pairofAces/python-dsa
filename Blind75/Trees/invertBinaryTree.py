from typing import List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: List[TreeNode]):
        # if there is no root, return None
        if not root:
            return None
        
        # swap the node values
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively call the function to the children nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

root = [4,2,7,1,3,6,9]

r = Solution()

print(r.invertTree(root))