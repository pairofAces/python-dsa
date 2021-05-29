# BREADTH FIRST SEARCH

# PROMPT

# Given a Node class that has a name and an array of children nodes,
# which are optional. When the nodes are put together, they form a
# tree like structure. 

# implement the breadthFirstSearch method on the Node class, which takes 
# an empty array, traverses the tree using the breadth first search approach,
# from left-to-right, and stores all the nodes' names in the input array,
# and finall returning the array.

# Solution 

class Node:
    def__init__(self, name):
        sef.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self, array):
