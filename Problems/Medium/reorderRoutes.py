from pip import List
# Leetcode 1466

# Reorder routes to make all paths lead to city zero

# there are (n) cities numbered 0 to (n-1) and (n-1) roads such that
# there is only one way to travel between cities. 
# Last year, the ministry of transport decided to orient the roads in one direction
# because they're too narrow. 

# Roads are represented by (connections) where connections[i] = [a ,b]
# represents a road from city (a) to (b).

# There's going to be a big event in (city 0) 

# your task consists of reorienting the roads so that each city can visit
# (city 0). Return the minimum number of edges changed.

# # it's guaranteed that each city can reach (city 0) after the reorder



class Solution:
    def minReorder(self, n: int, connections: List[List[int]]):
        # start at city 0
        # recursively check the neighbor nodes
        # count the number of outgoing edges
        
        edges = { (a, b) for a, b in connections}
        neighbors = { city:[] for city in range(n)}
        visit = set()
        changes = 0

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # create a helper method
        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                # check if this neighbor can reach (city 0)
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes