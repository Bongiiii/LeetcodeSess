"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #dfs clone helper function
        #hashmap to keep the visited nodes
        visited = defaultdict()

        def clone(node):
            #base cases
            #empty graph
            if node is None:
                return

            #already visited node
            if node in visited:
                return visited[node]

            #make a new node by cloning thhe original node
            cloneNode = Node(node.val)

            #map original to the cloned node
            visited[node] = cloneNode

            # For every adjacent node, create a clone copy to the neighbors of the cloned node
            for neighbor in node.neighbors:
                cloneNode.neighbors.append(clone(neighbor))

            return cloneNode

        # Start the graph cloning process from the input node
        return clone(node)
