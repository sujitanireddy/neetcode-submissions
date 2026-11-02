class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) >= n:
            return False

        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visit = set()

        def dfs(node):

            if node in visit:
                return False
            
            visit.add(node)

            for nei in adjList[node]:
                dfs(nei)

            return True

        if not dfs(0):
            return False

        return len(visit) == n
        
