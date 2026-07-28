"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldtonew = {}

        def dfs(node):

            if not node:
                return
            
            if node in oldtonew:
                return oldtonew[node]

            new_node = Node(node.val)
            oldtonew[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return oldtonew[node]
        
        return dfs(node)