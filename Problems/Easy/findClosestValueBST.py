# Find the closest value in Binary Search Tree

# create a function that takes in a BST and a target integer value
# and return the value that's closest to the target integer in the BST.

    # assume there's only one closest value

#  BOTH SOLUTIONS USE THE BST CLASS BELOW
    # this is the class of the input tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution 1
    # Complexity
        # Average Time: O(log(n)) time
        # Average Space: O(log(n)) space

        # Worst case Time: O(n) time
        # Worst case Space: O(n) space

def findClosestValueInBst(tree, target):
    # create a helper method, then invoke within this function

# create helper function below
def bstHelper(tree, target, closest):
    # If there is no tree, return the closest value
    if tree is None:
        return closest
    
    # if the absolute value of the (target-closest) is greater than
    # (target-tree.value, then set (closest) to (tree.value)
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    
    # if (target) is less than (tree.value)
    # use recursion to invoke the bstHelper function with
    # the (tree.left) value, the (target), and the (closest)
    if target < tree.value:
        return bstHelper(tree.left, target, closest)

    # if (target) is greater than (tree.value)
    # use recursion to invoke the bstHelper function with
    # the (tree.right) value, the (target), and the (closest)
    elif target > tree.value:
        return bstHelper(tree.right, target, closest)

    # otherwise, return the closest value
    else:
        return closest

# ------------------------------------------------------------------------

# Solution 2 - Optimized

def findClosestValueInBst(tree, target):
    # aspirational code - helper function
    return findClosestValueHelper(tree, target, tree.value)

# create helper function below
def findClosestValueHelper(tree, target, closest):
