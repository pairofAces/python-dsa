# BINARY SEARCH TREE TRAVERSAL

# create three functions that take in a Binary Search Tree (BST) and an 
# empty array , traverse the BST, add it's nodes values to the input
# array, and then return that array. 

# The functions should traverse the the BST using the in-order, 
# pre-order, and post-order tree-traversal techniques, respectively.

class Solution:
    def inOrderTraverse(tree, array):
        # if the tree input isn't (None)
            # use recursion to make a recurive function call
            # to (inOrderTraverse), to find the left and right
            # child nodes, then add them to the empty input array
            # and add the current node as well
        if tree is not None:
            inOrderTraverse(tree.left, array)
            array.append(tree.value)
            inOrderTraverse(tree.right, array)
        
        # return the array
        return array

    # the following class methods, will be using similar logic as above
    def preOrderTraverse(tree, array):
        # if the tree isn't (None)
            # append the value of the current node
            # call the method using the left child node as the first input, and array
            # call the method using the right child node as the first input, and array
            array.append(tree.value)
            preOrderTraverse(tree.left, array)
            preOrderTraverse(tree.right, array)
        
        # now return the array with its values
        return array

    def postOrderTraversal(tree, array):
        # if the tree isn't (None)
            # call the method with the left child node as the first input, and the array
            # then call the method with the right child node as the first input, and the array
            # then append the value of the current node, to the input array
        