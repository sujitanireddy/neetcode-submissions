"""
- no cycles
- all nodes are connected
{
  0 : [1,2,3]
  1 : [0,4]
  2 : [0]
  3 : [0]
  4 : [1]
}

visit = {0,1}

dfs(0) = {0}      -> dfs(2) = {0,1,4,2} -> dfs(3) = {0,1,4,2,3}
dfs(1) = {0,1}
dfs(4) = {0,1,4}
------------------
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges: return True 

        if len(edges) >= n:
            return False
        
        adjList = {i : [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        
        def dfs(c):
            
            visit.add(c)
            
            for nei in adjList[c]:
                if nei not in visit:
                    dfs(nei)
        
        dfs(0)
        
        return len(visit) == n