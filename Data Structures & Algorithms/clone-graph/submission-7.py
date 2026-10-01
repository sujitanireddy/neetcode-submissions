"""
int val
neighbors = []

 1                      2
[2] ----------------- [1,3]
                        |
                        |
                        |
                        |
                        |
                        |
                        3
                       [2]

Brute Force Way:
- Build adjList while exploring the graph 
- Use adjList to build a deep copy

{
    1   : [2]
    2   : [1,3]
    3   : [2]
}

TC: O(V+E)
SC: O(V+E)


old_to_new 

{
    1   :   &1

}


"""
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
            
            if node in old_to_new:
                return old_to_new[node]
            
            new_node = Node(node.val)
            old_to_new[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node
        

        return dfs(node)







































        