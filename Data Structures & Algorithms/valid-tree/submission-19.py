class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) >= n:
            return False
        
        adjList = {i: [] for i in range(n)}

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()

        def dfs(i):

            if i in visit:
                return

            visit.add(i)
            
            for nei in adjList[i]:
                dfs(nei)

        dfs(0)

        return len(visit) == n