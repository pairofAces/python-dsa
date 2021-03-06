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

    # Comlexity Analysis
        # Time: O(v + e) time, where (v) is the number of vertices, and (e)
        #       is the number of edges on the graph.

        # Space: O(v) space
class Node:
    def__init__(self, name):
        sef.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self, array):
        # create a variable to represent a duplicate of (self)
        # as an array
        queue = [self]

        # while the length of the queue is greater than 0
        while len(queue) > 0:

            # create a variable to represent the first element in (queue)
            current = queue.pop(0)

            # append current to the input array
            array.append(current.name)

            # for each children of (current)
            for child of current.children:
                # append the (child) to the queue
                queue.append(child)
        
        # once out of the while loop, return the array
        return array