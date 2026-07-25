"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        oldtoNew = {}

        def dfs(node):

            if node in oldtoNew:
                return oldtoNew[node]

            new_node = Node(node.val)
            
            oldtoNew[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return oldtoNew[node]

        return dfs(node)