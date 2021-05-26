# INVERT BINARY TREE

# PROMPT

# create a function that takes in a Binary Tree and inverts it. 
    # the function should swap every left node in the tree for its
    # corresponding right node.

class Solution:
    def invertBinaryTree(tree):
        # create an array variable that will take in the (tree) input
        queue = [tree]

        # initiate a while loop, for the length of the (queue)
        while len(queue):
            # create a variable to represent the first element in the (queue)
            current = queue.pop(0)



# create the Binary Tree class
class BinaryTree:
    def__init__(self, value):
        self.value = value
        self.left = None
        self.right = None
