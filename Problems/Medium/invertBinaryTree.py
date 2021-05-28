# INVERT BINARY TREE

# PROMPT

# create a function that takes in a Binary Tree and inverts it. 
    # the function should swap every left node in the tree for its
    # corresponding right node.

# Solution 1
class Solution:
    def invertBinaryTree(tree):
        # create an array variable that will take in the (tree) input
        queue = [tree]

        # initiate a while loop, for the length of the (queue)
        while len(queue):
            # create a variable to represent the first element in the (queue)
            current = queue.pop(0)
        
        # use an if statement, just in case (current) might be None
        if current is None:
            # then simply continue
            continue
        
        # aspirational code, to handle swapping the child nodes
        swapHelper(current)

        # append the left and right child nodes to the (queue)
        queue.append(current.left)
        queue.append(current.right)

    def swapHelper(tree):
        tree.left, tree.right = tree.right, tree.left


# create the Binary Tree class
class BinaryTree:
    def__init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution 2 -> using recursion
    # COMPLEXITY ANALYSIS:
        # TIME: O(n) time, where (n) is the number of nodes

        # SPACE: O(d) space, where (d) is the depth of the tree

class Solution2:
    def invertBinaryTree(tree):
        # if there is no tree
        if tree is None:
            return
        # use the same logic as the (swapHelper) function in (solution1)
        swapHandler(tree)

        # use recursion, call the (invertBinaryTree) function on the left and
        # right child of the (tree) input
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    
    # create a swapHandler function below
    def swapHandler(tree):
        tree.left, tree.right = tree.right, tree.left