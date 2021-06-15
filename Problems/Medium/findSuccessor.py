# Find Successor

# create a function that takes in a Binary Tree (where nodes have an
# additional pointer to their parent node) as well as a node contained
# in that tree and returns the given node's successor

    # Note, a successor is the next node to be visited(immediately
    # after the given node) when traversing its tree using the in-order
    # tree-traversal technique.

class BinaryTree:
    def__init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def findSuccessor(tree, node):
        