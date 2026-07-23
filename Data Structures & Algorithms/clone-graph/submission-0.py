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
        
        adjList = defaultdict(list) #val : [neighbors]
        visit = set()

        def dfs(node, adjList, visit):

            adjList[node] = Node(node.val)
            visit.add(node)

            for neighbor in node.neighbors:
                if neighbor not in visit:
                    dfs(neighbor, adjList, visit)
        
        dfs(node, adjList, visit)

        for old, new in adjList.items():
            for neighbor in old.neighbors:
                new.neighbors.append(adjList[neighbor])
        
        return adjList[node]

                     