"""

Valid Tree = Edges = Vertices - 1



"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) >= n:
            return False
        
        adjList = {i:[] for i in range(n)}

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()

        def dfs(node):
            
            visit.add(node)

            for nei in adjList[node]:
                if nei not in visit:
                    dfs(nei)
        
        dfs(0)
        return len(visit) == n
