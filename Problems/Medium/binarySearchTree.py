# Binary Search Tree Construction

# create a BST class that supports the following:
    # inserting values with the insert method
    # removing values with the remove method
    # searching for values with the contains method

class BST:
    # initialize
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # create the inset method
    def insert(self, value):
        # if the value is less than the originally initialized value
        # then the left value will become the new, lower value

        # else, if the value is greater than the initialized value, the
        # right value will be set to the new, greater value
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
    
    # create the remove method
    def remove(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.vlue:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                # create a helper function to set the value
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.right = self.right.left
                    self.left = self.right.right
                else:
                    # since this is a single node tree, do nothing
                    pass
        return self

    # create the contains method
    def contains(self, value):
        # if the value is less than the initialized value
        if value < self.value:
            # if there is no left value, then False
            if self.left is None:
                return False
            else:
            # otherwise, check if the left has the given value
                return self.left.contains(value)
                
        # if the value is greater than the initialized value
        elif value > self.value:
            # if there is no right value, then False
            if self.right is None:
                return False
            
            # otherwise, check if the right has the given value
            else:
                return self.right.contains(value)

        # if the given value is found, then True
        else:
            return True