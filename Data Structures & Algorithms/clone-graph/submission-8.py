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
        
        old_to_new = defaultdict()

        def dfs(node):
            
            #base case
            if node in old_to_new:
                return old_to_new[node]

            val = node.val
            new_node = Node(val)
            old_to_new[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node

        return dfs(node)
