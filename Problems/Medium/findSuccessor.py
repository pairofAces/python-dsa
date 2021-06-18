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


# Complexity Analysis
    # Time: O(n) time, where (n) is the number of nodes in the tree

    # Space: O(n) space, where (n) is the number of elements created in
    # array from the helper method
class Solution:
    def findSuccessor(tree, node):
        # aspirational code, create helper method to handle
        # building an array of the nodes
        inOrderTraverse = getInOrderTraversal(tree)

        # traverse through the array created in the helper method
        for i, currentNode in enumerate(inOrderTraverse):
            # if the (currentNode) isn't equal to the input (node)
            if currentNode != node:
                # then continue
                continue
            
            # if the index is equal to the length of the array created in
            # helper method
            if i == len(inOrderTraverse):
                return None
            
            # return the value of the inOderTraverse with the input of
            # the index + 1
            return inOderTraverse(i + 1)
    
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

class Solution2:
    def findSuccessor2(tree, node):
        # if there is a right node
        if node.right is not None:
            # aspirational code
                # helper method
            return getLeftmostChildNode(node.right)
        
        # aspirational code
            # helper method
        return getRightmostChildNode(node)
    
    # create helper methods below
    def getLeftmostChildNode(node):
        currentNode = node
        # while there is a left child node
        while currentNode.left is not None:
            currentNode = currentNode.left
        
        # return the value of (currentNode)
        return currentNode

    def getRightmostChildNode(node):
