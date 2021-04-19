# Depth-First Search

# Given a Node class that has a name and an array of optional children
# nodes, implement the depthFirstSearch method on the Node class, that
# takes an empty array and taverses the tree, from left-to-right, storing 
# all of the node names into the input array and return it. 

# create the node class
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        