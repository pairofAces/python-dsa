# Depth-First Search

# Given a Node class that has a name and an array of optional children
# nodes, implement the depthFirstSearch method on the Node class, that
# takes an empty array and taverses the tree, from left-to-right, storing 
# all of the node names into the input array and return it. 


# Solution
    # Complexity Analysis
        # Time: O(v + e), where (v) is the number of vertices on the graph
        # and (e) are the number of edges

        # Space: O(v) space, where (v) is the number of vertices,
        # whos names had to be appended to the input array
        
# create the node class
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        # append the name to the input array
        array.append(self.name)

        # for each node (child), invoke depthFirstSearch
        for child in self.children:
            child.depthFirstSearch(array)
        
        # return the final, mutated input array
        return array