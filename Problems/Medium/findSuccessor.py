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
        # aspirational code, create helper method to handle
        # building an array of the nodes
        inOrderTraverse = getInOrderTraversal(tree)

        # traverse through the array created in the helper method
        for i, currentNode in enumerate(inOrderTraverse):
            # if the (currentNode) isn't equal to the input (node)
            if currentNode != node:
                
    
    # helper function below
    def getInOrderTraversal(node, order = []):
        # if the node is None
        if node is None:
            return order
        
        # use recursion to apply the helper function to the left
        # and right nodes
        getInOrderTraversal(node.left, order)
        order.append(node)
        getInOrderTraversal(node.right, order)

        # return the final (order) array
        return order